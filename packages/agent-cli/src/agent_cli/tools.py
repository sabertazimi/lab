"""Tool definitions and execution for agent-cli.

This module defines all available tools and their execution logic.
Tools are decoupled from global state and accept dependencies as parameters.
"""

import fnmatch
import functools
import os
import re
import subprocess
import time
from collections.abc import Callable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

from anthropic.types import ToolParam

if TYPE_CHECKING:
    from .interfaces import IAgentUI
    from .skill import SkillLoader
    from .task import TaskManager


SpawnSubagentFn = Callable[[str, str, str], str]


@dataclass
class BashToolCall:
    name: Literal["Bash"]
    command: str


@dataclass
class ReadToolCall:
    name: Literal["Read"]
    path: str
    limit: int | None = None


@dataclass
class WriteToolCall:
    name: Literal["Write"]
    path: str
    content: str


@dataclass
class EditToolCall:
    name: Literal["Edit"]
    path: str
    old_text: str
    new_text: str


@dataclass
class GlobToolCall:
    name: Literal["Glob"]
    pattern: str
    path: str | None = None


@dataclass
class GrepToolCall:
    name: Literal["Grep"]
    pattern: str
    path: str | None = None
    output_mode: str | None = None
    glob: str | None = None
    i: bool | None = None
    n: bool | None = None
    head_limit: int | None = None
    offset: int | None = None


@dataclass
class WebSearchToolCall:
    name: Literal["WebSearch"]
    query: str
    allowed_domains: list[str] | None = None
    blocked_domains: list[str] | None = None


@dataclass
class WebReaderToolCall:
    name: Literal["WebReader"]
    url: str
    prompt: str


@dataclass
class TaskUpdateToolCall:
    name: Literal["TaskUpdate"]
    tasks: list[dict[str, str]]


@dataclass
class TaskToolCall:
    name: Literal["Task"]
    agent_type: str
    prompt: str
    description: str


@dataclass
class SkillToolCall:
    name: Literal["Skill"]
    skill_name: str


ToolCall = (
    BashToolCall
    | ReadToolCall
    | WriteToolCall
    | EditToolCall
    | GlobToolCall
    | GrepToolCall
    | WebSearchToolCall
    | WebReaderToolCall
    | TaskUpdateToolCall
    | TaskToolCall
    | SkillToolCall
)


CURRENT_DATE = datetime.now().strftime("%Y-%m-%d")


DEFAULT_EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".venv",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "dist",
    "build",
    ".next",
    ".nuxt",
    "coverage",
    ".tox",
    "eggs",
    ".eggs",
}

BASE_TOOLS: list[ToolParam] = [
    {
        "name": "Bash",
        "description": "Run a shell command. Use for: ls, find, grep, git, pnpm, uv, python, etc. Security: blocks dangerous commands. Output truncated to 50KB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "The shell command to execute",
                },
            },
            "required": ["command"],
        },
    },
    {
        "name": "Read",
        "description": "Read file content. Returns UTF-8 text. Path must be within workspace (security constraint). Output truncated to 50KB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path to the file",
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum lines to read (default: all)",
                },
            },
            "required": ["path"],
        },
    },
    {
        "name": "Write",
        "description": "Write content to a file, creating parent directories if needed. Path must be within workspace (security constraint). Use for complete file creation/overwrite. For partial changes, use Edit tool instead (safer).",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path for the file",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write",
                },
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "Edit",
        "description": "Replace exact text in a file (surgical edit). Path must be within workspace (security constraint). Only replaces first occurrence. Use for partial changes - safer than Write. For complete file rewrites, use Write tool instead.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Relative path to the file",
                },
                "old_text": {
                    "type": "string",
                    "description": "Exact text to find (must match precisely)",
                },
                "new_text": {
                    "type": "string",
                    "description": "Replacement text",
                },
            },
            "required": ["path", "old_text", "new_text"],
        },
    },
    {
        "name": "Glob",
        "description": "Fast file pattern matching. Returns files sorted by modification time (newest first). Works with any codebase size. Output truncated to 50KB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string",
                    "description": "Glob pattern to match files (e.g., '**/*.js', 'src/**/*.ts', '*.{json,yaml}')",
                },
                "path": {
                    "type": "string",
                    "description": "Directory to search in. Defaults to current working directory. IMPORTANT: Omit this field entirely to use the default directory.",
                },
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "Grep",
        "description": "Powerful search tool for finding text/code patterns in files. Supports regex, glob filtering, case-insensitive search, and multiple output modes. Output truncated to 50KB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "pattern": {
                    "type": "string",
                    "description": "Regular expression to search for. Uses Python regex syntax. Literal braces need escaping: interface\\{\\} to find interface{}.",
                },
                "path": {
                    "type": "string",
                    "description": "File or directory to search. Defaults to current directory.",
                },
                "output_mode": {
                    "type": "string",
                    "enum": ["content", "files_with_matches", "count"],
                    "description": "Output format: 'content' shows matching lines with line numbers (default, use when you need to see matches); 'files_with_matches' shows only file paths (use when you don't need line details); 'count' shows match counts per file (use when quantifying results).",
                },
                "glob": {
                    "type": "string",
                    "description": "Filter files by glob pattern (e.g., '*.js', '**/*.py').",
                },
                "i": {
                    "type": "boolean",
                    "description": "Case insensitive search.",
                },
                "n": {
                    "type": "boolean",
                    "description": "Show line numbers (default: true, requires output_mode: 'content').",
                },
                "head_limit": {
                    "type": "integer",
                    "description": "Limit output to first N results.",
                },
                "offset": {
                    "type": "integer",
                    "description": "Skip first N results before applying head_limit.",
                },
            },
            "required": ["pattern"],
        },
    },
    {
        "name": "WebSearch",
        "description": f"""Search the web for current information beyond the knowledge cutoff. Returns up to 10 results as markdown with title links and snippets.
IMPORTANT: Today's date is {CURRENT_DATE} - use this date when forming queries for time-sensitive information. US only. Output truncated to 50KB.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query string (min 2 characters)",
                },
                "allowed_domains": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Array of domains to include in results (e.g., ['github.com', 'docs.python.org'])",
                },
                "blocked_domains": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Array of domains to exclude from results (e.g., ['pinterest.com', 'youtube.com'])",
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "WebReader",
        "description": "Fetch and process web content. Converts HTML to markdown. Auto-upgrades HTTP to HTTPS. Has a 15-minute cache. Read-only operation. Output truncated to 50KB.",
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "Fully-formed valid URL to fetch",
                },
                "prompt": {
                    "type": "string",
                    "description": "Context for what information you're looking for (note: currently for informational purposes only - full markdown is returned).",
                },
            },
            "required": ["url", "prompt"],
        },
    },
    {
        "name": "TaskUpdate",
        "description": "Update the task list. Use to plan and track progress.",
        "input_schema": {
            "type": "object",
            "properties": {
                "tasks": {
                    "type": "array",
                    "description": "Complete list of tasks (replaces existing list)",
                    "items": {
                        "type": "object",
                        "properties": {
                            "content": {
                                "type": "string",
                                "description": "Task description",
                            },
                            "status": {
                                "type": "string",
                                "enum": ["pending", "in_progress", "completed"],
                                "description": "Task status",
                            },
                            "active_form": {
                                "type": "string",
                                "description": "Present tense action, e.g. 'Reading files'",
                            },
                        },
                        "required": ["content", "status", "active_form"],
                    },
                },
                "list_title": {
                    "type": "string",
                    "description": "Short title (3-5 words) for task list",
                },
            },
            "required": ["tasks", "list_title"],
        },
    },
]


def build_task_tool(agent_types: dict[str, dict[str, str | list[str]]]) -> ToolParam:
    """Build the Task tool definition with agent type descriptions.

    Args:
        agent_types: Dictionary of agent type configurations.

    Returns:
        Task tool parameter definition.
    """
    from .subagent import get_agent_description

    return {
        "name": "Task",
        "description": f"""Spawn a subagent for a focused subtask.

Subagents run in ISOLATED context - they don't see parent's history.
Use this to keep the main conversation clean.

Agent types:
{get_agent_description()}

Example uses:
- Task(Explore): "Find all files using the auth module"
- Task(Plan): "Design a migration strategy for the database"
- Task(Code): "Implement the user registration form"
""",
        "input_schema": {
            "type": "object",
            "properties": {
                "agent_type": {
                    "type": "string",
                    "enum": list(agent_types.keys()),
                    "description": "The type of agent to spawn",
                },
                "prompt": {
                    "type": "string",
                    "description": "Detailed instructions for the subagent",
                },
                "description": {
                    "type": "string",
                    "description": "Short task name (3-5 words) for progress display",
                },
            },
            "required": ["agent_type", "prompt", "description"],
        },
    }


def build_skill_tool(skill_loader: SkillLoader) -> ToolParam:
    """Build the Skill tool definition with available skills.

    Args:
        skill_loader: Skill loader instance.

    Returns:
        Skill tool parameter definition.
    """
    return {
        "name": "Skill",
        "description": f"""<skills_instructions>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively.

How to use skills:
- Invoke skills using this tool with the skill name only (no arguments)
- The skill content will be injected into the conversation, giving you detailed instructions and access to resources.

When to use skills:
- IMMEDIATELY when user task matches a skill description
- Before attempting domain-specific work (PDF, MCP, etc.)

IMPORTANT:
- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already running
</skills_instructions>

<available_skills>
{skill_loader.get_descriptions()}
</available_skills>""",
        "input_schema": {
            "type": "object",
            "properties": {
                "skill_name": {
                    "type": "string",
                    "description": "The name of the skill to load",
                },
            },
            "required": ["skill_name"],
        },
    }


def build_all_tools(skill_loader: SkillLoader) -> list[ToolParam]:
    """Build the complete list of tools including Task and Skill.

    Args:
        skill_loader: Skill loader instance.

    Returns:
        Complete list of tool parameter definitions.
    """
    from .subagent import AGENTS

    return BASE_TOOLS + [build_task_tool(AGENTS), build_skill_tool(skill_loader)]


def safe_path(path: str, workdir: Path) -> Path:
    """Ensure path stays within workspace (security measure).

    Prevents the model from accessing files outside the project directory.
    Resolves relative paths and checks they don't escape via '../'.

    Args:
        path: Relative path string.
        workdir: Working directory to resolve against.

    Returns:
        Resolved absolute path.

    Raises:
        ValueError: If path escapes workspace.
    """
    resolved_path = (workdir / path).resolve()
    if not resolved_path.is_relative_to(workdir):
        raise ValueError(f"Path escapes workspace: {path}")
    return resolved_path


def run_bash(command: str | None, workdir: Path, timeout: float = 60) -> str:
    """Execute shell command with safety checks.

    Security: Blocks obviously dangerous commands.
    Timeout: 60 seconds to prevent hanging.
    Output: Truncated to 50KB to prevent context overflow.

    On Windows, uses git-bash for better Unix command compatibility.

    Args:
        command: Shell command to execute.
        workdir: Working directory for command execution.
        timeout: Command timeout in seconds (default: 60).

    Returns:
        Command output or error message.
    """
    if command is None:
        return "Error: Command is required"

    dangerous_commands = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(dangerous in command for dangerous in dangerous_commands):
        return "Error: Dangerous command blocked"

    try:
        if os.name == "nt":
            # Windows: use git-bash for Unix command compatibility
            result = subprocess.run(
                [r"C:\Program Files\Git\bin\bash.exe", "-c", command],
                cwd=workdir,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        else:
            # Unix-like: use default shell
            result = subprocess.run(
                command,
                shell=True,
                cwd=workdir,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        output = (result.stdout + result.stderr).strip()
        return output[:50000] if output else "(no output)"
    except subprocess.TimeoutExpired:
        return f"Error: Command timed out ({timeout}s)"
    except Exception as e:
        return f"Error: {e}"


def run_read(path: str, workdir: Path, limit: int | None = None) -> str:
    """Read file content with optional line limit.

    For large files, use limit to read just the first N lines.
    Output truncated to 50KB to prevent context overflow.

    Args:
        path: Relative path to the file.
        workdir: Working directory.
        limit: Maximum lines to read (default: all).

    Returns:
        File content or error message.
    """
    try:
        text = safe_path(path, workdir).read_text(encoding="utf-8", newline="\n")
        lines = text.splitlines()
        total_lines = len(lines)

        if limit is not None and limit > 0 and limit < total_lines:
            lines = lines[:limit]
            lines.append(f"... ({total_lines - limit} more lines)")

        return "\n".join(lines)[:50000]
    except Exception as e:
        return f"Error: {e}"


def run_write(path: str, content: str, workdir: Path) -> str:
    """Write content to a file, creating parent directories if needed.

    This is for complete file creation/overwrite.
    For partial edits, use Edit tool instead.

    Args:
        path: Relative path for the file.
        content: Content to write.
        workdir: Working directory.

    Returns:
        Success message or error.
    """
    try:
        file_path = safe_path(path, workdir)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8", newline="\n")
        return f"Wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"Error: {e}"


def run_edit(path: str, old_text: str, new_text: str, workdir: Path) -> str:
    """Replace exact text in a file (surgical edit).

    Uses exact string matching - the old_text must appear verbatim.
    Only replaces the first occurrence to prevent accidental mass changes.

    Args:
        path: Relative path to the file.
        old_text: Exact text to find.
        new_text: Replacement text.
        workdir: Working directory.

    Returns:
        Success message or error.
    """
    try:
        file_path = safe_path(path, workdir)
        content = file_path.read_text(encoding="utf-8", newline="\n")

        if old_text not in content:
            return f"Error: Text not found in {path}"

        new_content = content.replace(old_text, new_text, 1)
        file_path.write_text(new_content, encoding="utf-8", newline="\n")
        return f"Edited {path}"
    except Exception as e:
        return f"Error: {e}"


def run_glob(pattern: str, workdir: Path, path: str | None = None) -> str:
    """Find files matching a glob pattern.

    Returns files sorted by modification time (newest first).
    Excludes common large/irrelevant directories for performance.
    Output truncated to 50KB to prevent context overflow.

    Args:
        pattern: Glob pattern to match.
        workdir: Working directory.
        path: Directory to search in (default: workdir).

    Returns:
        Matched files or error message.
    """
    try:
        search_path = safe_path(path or ".", workdir)

        all_files: list[Path] = []
        for root, dirnames, filenames in os.walk(search_path):
            # Prevent descending into excluded directories
            dirnames[:] = [d for d in dirnames if d not in DEFAULT_EXCLUDED_DIRS]
            for filename in filenames:
                all_files.append(Path(root) / filename)

        # Filter by glob pattern
        matched_files = [f for f in all_files if fnmatch.fnmatch(str(f), f"*{pattern}")]
        files = sorted(matched_files, key=lambda p: p.stat().st_mtime, reverse=True)
        result = "\n".join(str(f) for f in files)
        return result[:50000] if result else "(no matches)"
    except Exception as e:
        return f"Error: {e}"


def run_grep(
    pattern: str,
    workdir: Path,
    path: str | None = None,
    output_mode: str = "content",
    glob: str | None = None,
    i: bool = False,
    n: bool = True,
    head_limit: int = 0,
    offset: int = 0,
) -> str:
    """Search for pattern in files using pure Python regex.

    Supports multiple output modes and filtering options.
    Output truncated to 50KB to prevent context overflow.

    Args:
        pattern: Regex pattern to search for.
        workdir: Working directory.
        path: File or directory to search (default: workdir).
        output_mode: Output format (content/files_with_matches/count).
        glob: Filter files by glob pattern.
        i: Case insensitive search.
        n: Show line numbers.
        head_limit: Limit output to first N results.
        offset: Skip first N results.

    Returns:
        Search results or error message.
    """
    try:
        flags = re.IGNORECASE if i else 0
        try:
            regex = re.compile(pattern, flags)
        except re.error:
            return f"Error: Invalid regex pattern: {pattern}"

        search_path = safe_path(path or ".", workdir)

        if search_path.is_file():
            files = [search_path]
        else:
            all_files: list[Path] = []
            for root, dirnames, filenames in os.walk(search_path):
                # Prevent descending into excluded directories
                dirnames[:] = [d for d in dirnames if d not in DEFAULT_EXCLUDED_DIRS]
                for filename in filenames:
                    all_files.append(Path(root) / filename)

            # Filter by glob pattern if specified
            if glob:
                files = [f for f in all_files if fnmatch.fnmatch(f.name, glob)]
            else:
                files = all_files

        content_matches: list[str] = []
        file_matches: set[str] = set()
        count_matches: dict[str, int] = {}

        for file_path in files:
            try:
                # Read file and search line by line
                text = file_path.read_text(encoding="utf-8", errors="ignore")
                lines = text.splitlines()

                for line_num, line in enumerate(lines, 1):
                    if regex.search(line):
                        file_matches.add(str(file_path))
                        count_matches[str(file_path)] = (
                            count_matches.get(str(file_path), 0) + 1
                        )

                        if output_mode == "content":
                            if n:
                                content_matches.append(f"{file_path}:{line_num}:{line}")
                            else:
                                content_matches.append(f"{file_path}:{line}")

                # Stop early if reached head_limit (excluding offset)
                if (
                    output_mode == "content"
                    and head_limit > 0
                    and len(content_matches) >= head_limit + offset
                ):
                    break

            except (OSError, UnicodeDecodeError):
                continue

        # Format output based on mode
        if output_mode == "content":
            result = "\n".join(content_matches)
            if offset > 0:
                lines_list = result.splitlines()
                result = "\n".join(lines_list[offset:])
            if head_limit > 0:
                lines_list = result.splitlines()
                result = "\n".join(lines_list[:head_limit])
        elif output_mode == "files_with_matches":
            result = "\n".join(sorted(file_matches))
        elif output_mode == "count":
            lines_list = [f"{f}:{count}" for f, count in sorted(count_matches.items())]
            result = "\n".join(lines_list)
        else:
            result = f"Error: Unknown output_mode '{output_mode}'"

        return result[:50000] if result else "(no matches)"
    except Exception as e:
        return f"Error: {e}"


def run_web_search(
    query: str,
    allowed_domains: list[str] | None = None,
    blocked_domains: list[str] | None = None,
) -> str:
    """Search the web using DuckDuckGo.

    Returns results as markdown with title links and snippets.
    Output truncated to 50KB to prevent context overflow.

    Args:
        query: Search query string.
        allowed_domains: Domains to include in results.
        blocked_domains: Domains to exclude from results.

    Returns:
        Search results or error message.
    """
    try:
        from ddgs import DDGS  # type: ignore 3rd-party package

        ddgs = DDGS()
        results = ddgs.text(query, max_results=10)

        if not results:
            return "(no results)"

        # Filter by domains if specified
        if allowed_domains:
            results = [
                r
                for r in results
                if any(d in r.get("href", "") for d in allowed_domains)
            ]
        if blocked_domains:
            results = [
                r
                for r in results
                if not any(d in r.get("href", "") for d in blocked_domains)
            ]

        # Format as markdown
        formatted: list[str] = []
        for r in results:
            title = r.get("title", "")
            url = r.get("href", "")
            body = r.get("body", "")
            formatted.append(f"## [{title}]({url})\n\n{body}")

        output = "\n\n".join(formatted)
        return output[:50000]
    except Exception as e:
        return f"Search failed: {e}"


@functools.lru_cache(maxsize=128)
def fetch_cached(url: str, cache_time: int) -> str:
    """Cached fetch with timestamp to invalidate after 15 minutes."""
    return fetch_uncached(url)


def fetch_uncached(url: str) -> str:
    """Fetch and convert HTML to markdown."""
    import httpx
    from markdownify import markdownify as md

    # Auto-upgrade HTTP to HTTPS
    if url.startswith("http://"):
        url = url.replace("http://", "https://", 1)

    response = httpx.get(url, follow_redirects=True, timeout=30)
    response.raise_for_status()

    # Convert HTML to markdown
    return md(response.text)


def run_web_fetch(url: str, prompt: str) -> str:
    """Fetch web content and convert to markdown.

    Uses 15-minute cache for repeated requests.
    Output truncated to 50KB to prevent context overflow.

    Args:
        url: URL to fetch.
        prompt: Context for the fetch (informational).

    Returns:
        Markdown content or error message.
    """
    try:
        # 15-minute cache (900 seconds)
        cache_time = int(time.time() / 900)
        content = fetch_cached(url, cache_time)

        # Note: The prompt is for context - full implementation would pass to LLM
        # For now, return raw markdown content
        return content[:50000]
    except Exception as e:
        return f"Fetch failed: {e}"


def run_task_update(tasks: list[dict[str, str]], task_manager: TaskManager) -> str:
    """Update the task list.

    The model sends a complete new list (not a diff).
    We validate it and return the rendered view.

    Args:
        tasks: List of task dictionaries.
        task_manager: Task manager instance.

    Returns:
        Rendered task list or error message.
    """
    try:
        return task_manager.update(tasks)
    except Exception as e:
        return f"Error: {e}"


def run_skill(skill_name: str, skill_loader: SkillLoader) -> str:
    """Load a skill and inject it into the conversation.

    This is the key mechanism:
    1. Get skill content (SKILL.md body + resource hints)
    2. Return it wrapped in <skill-loaded> tags
    3. Model receives this as tool_result (user message)
    4. Model now "knows" how to do the task

    Args:
        skill_name: Name of the skill to load.
        skill_loader: Skill loader instance.

    Returns:
        Skill content or error message.
    """
    content = skill_loader.get_skill(skill_name)

    if content is None:
        available_skills = ", ".join(skill_loader.list_skills()) or "none"
        return (
            f"Error: Unknown skill '{skill_name}'. Available skills: {available_skills}"
        )

    return f"""<skill-loaded name="{skill_name}">
{content}
</skill-loaded>

Follow the instructions in the skill above to complete the user's task."""


def execute_tool(
    ui: IAgentUI,
    name: str,
    args: dict[str, object],
    *,
    workdir: Path,
    skill_loader: SkillLoader,
    spawn_subagent: SpawnSubagentFn | None = None,
    task_manager: TaskManager | None = None,
) -> str:
    """Dispatch tool call to the appropriate implementation.

    This is the bridge between the model's tool calls and the actual execution.
    Each tool returns a string result that goes back to the model.

    Args:
        ui: UI interface for output (currently unused but kept for consistency).
        name: Tool name.
        args: Tool arguments.
        workdir: Working directory.
        skill_loader: Skill loader instance.
        spawn_subagent: Optional callback to spawn subagents.
        task_manager: Optional task manager instance.

    Returns:
        Tool execution result.
    """
    match name:
        case "Bash":
            tool = BashToolCall(name="Bash", command=str(args["command"]))
            return run_bash(tool.command, workdir)
        case "Read":
            limit = args.get("limit")
            tool = ReadToolCall(
                name="Read",
                path=str(args["path"]),
                limit=int(limit) if isinstance(limit, (int, float, str)) else None,
            )
            return run_read(tool.path, workdir, tool.limit)
        case "Write":
            tool = WriteToolCall(
                name="Write", path=str(args["path"]), content=str(args["content"])
            )
            return run_write(tool.path, tool.content, workdir)
        case "Edit":
            tool = EditToolCall(
                name="Edit",
                path=str(args["path"]),
                old_text=str(args["old_text"]),
                new_text=str(args["new_text"]),
            )
            return run_edit(tool.path, tool.old_text, tool.new_text, workdir)
        case "Glob":
            tool = GlobToolCall(
                name="Glob",
                pattern=str(args["pattern"]),
                path=str(args["path"]) if "path" in args else None,
            )
            return run_glob(tool.pattern, workdir, tool.path)
        case "Grep":
            tool = GrepToolCall(
                name="Grep",
                pattern=str(args["pattern"]),
                path=str(args["path"]) if "path" in args else None,
                output_mode=str(args["output_mode"]) if "output_mode" in args else None,
                glob=str(args["glob"]) if "glob" in args else None,
                i=bool(args["i"]) if "i" in args else None,
                n=bool(args["n"]) if "n" in args else None,
                head_limit=int(cast(int | float | str, args["head_limit"]))
                if "head_limit" in args
                else None,
                offset=int(cast(int | float | str, args["offset"]))
                if "offset" in args
                else None,
            )
            return run_grep(
                tool.pattern,
                workdir,
                tool.path,
                tool.output_mode if tool.output_mode is not None else "content",
                tool.glob,
                tool.i if tool.i is not None else False,
                tool.n if tool.n is not None else True,
                tool.head_limit if tool.head_limit is not None else 0,
                tool.offset if tool.offset is not None else 0,
            )
        case "WebSearch":
            allowed = (
                [str(x) for x in cast(list[object], args["allowed_domains"])]
                if "allowed_domains" in args
                else None
            )
            blocked = (
                [str(x) for x in cast(list[object], args["blocked_domains"])]
                if "blocked_domains" in args
                else None
            )
            tool = WebSearchToolCall(
                name="WebSearch",
                query=str(args["query"]),
                allowed_domains=allowed,
                blocked_domains=blocked,
            )
            return run_web_search(
                tool.query, tool.allowed_domains, tool.blocked_domains
            )
        case "WebReader":
            tool = WebReaderToolCall(
                name="WebReader",
                url=str(args["url"]),
                prompt=str(args["prompt"]),
            )
            return run_web_fetch(tool.url, tool.prompt)
        case "TaskUpdate":
            if task_manager is None:
                return "Error: TaskUpdate not available in this context"
            tasks = cast(list[dict[str, str]], args.get("tasks", []))
            tool = TaskUpdateToolCall(name="TaskUpdate", tasks=tasks)
            return run_task_update(tool.tasks, task_manager)
        case "Task":
            if spawn_subagent is None:
                return "Error: Task tool not available in this context"
            tool = TaskToolCall(
                name="Task",
                agent_type=str(args["agent_type"]),
                prompt=str(args["prompt"]),
                description=str(args["description"]),
            )
            return spawn_subagent(tool.agent_type, tool.prompt, tool.description)
        case "Skill":
            tool = SkillToolCall(name="Skill", skill_name=str(args["skill_name"]))
            return run_skill(tool.skill_name, skill_loader)
        case _:
            return f"Unknown tool: {name}"
