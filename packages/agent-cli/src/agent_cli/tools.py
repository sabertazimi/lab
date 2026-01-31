import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Literal, cast

from anthropic.types import (
    MessageParam,
    TextBlock,
    ToolParam,
    ToolResultBlockParam,
    ToolUseBlock,
)

from .agent import AGENTS, get_agent_description
from .llm import MODEL, WORKDIR, client
from .output import get_tool_call_detail
from .skill import skill_loader
from .task import task_manager

if TYPE_CHECKING:
    from .tui import AgentApp


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
    | TaskUpdateToolCall
    | TaskToolCall
    | SkillToolCall
)


BASE_TOOLS: list[ToolParam] = [
    {
        "name": "Bash",
        "description": "Run a shell command. Use for: ls, find, grep, git, pnpm, uv, python, etc.",
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
        "description": "Read file content. Return UTF-8 text.",
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
        "description": "Write content to a file. Create parent directories if needed.",
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
        "description": "Replace exact text in a file. Use for surgical edits.",
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
                "description": {
                    "type": "string",
                    "description": "Short title (3-5 words) for task list",
                },
            },
            "required": ["tasks", "description"],
        },
    },
]

TASK_TOOL: ToolParam = {
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
                "enum": list(AGENTS.keys()),
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

SKILL_TOOL: ToolParam = {
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

ALL_TOOLS = BASE_TOOLS + [TASK_TOOL, SKILL_TOOL]


def safe_path(path: str) -> Path:
    """
    Ensure path stays within workspace (security measure).

    Prevents the model from accessing files outside the project directory.
    Resolves relative paths and checks they don't escape via '../'.
    """
    resolved_path = (WORKDIR / path).resolve()
    if not resolved_path.is_relative_to(WORKDIR):
        raise ValueError(f"Path escapes workspace: {path}")
    return resolved_path


def get_tools_for_agent(agent_type: str) -> list[ToolParam]:
    """
    Filter tools based on agent type.

    Each agent type has a whitelist of allowed tools.
    '*' means all tools (but subagents don't get Task to prevent infinite recursion).
    """
    allowed_tools = AGENTS.get(agent_type, {}).get("tools", "*")

    if allowed_tools == "*":
        return BASE_TOOLS

    return [tool for tool in BASE_TOOLS if tool["name"] in allowed_tools]


def run_bash(command: str, timeout: float = 60) -> str:
    """
    Execute shell command with safety checks.

    Security: Blocks obviously dangerous commands.
    Timeout: 60 seconds to prevent hanging.
    Output: Truncated to 50KB to prevent context overflow.

    On Windows, uses git-bash for better Unix command compatibility.
    """
    dangerous_commands = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(dangerous in command for dangerous in dangerous_commands):
        return "Error: Dangerous command blocked"

    try:
        if os.name == "nt":
            # Windows: use git-bash for Unix command compatibility
            result = subprocess.run(
                [r"C:\Program Files\Git\bin\bash.exe", "-c", command],
                cwd=WORKDIR,
                capture_output=True,
                text=True,
                timeout=timeout,
            )
        else:
            # Unix-like: use default shell
            result = subprocess.run(
                command,
                shell=True,
                cwd=WORKDIR,
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


def run_read(path: str, limit: int | None = None) -> str:
    """
    Read file content with optional line limit.

    For large files, use limit to read just the first N lines.
    Output truncated to 50KB to prevent context overflow.
    """
    try:
        text = safe_path(path).read_text(encoding="utf-8", newline="\n")
        lines = text.splitlines()
        total_lines = len(lines)

        if limit is not None and limit > 0 and limit < total_lines:
            lines = lines[:limit]
            lines.append(f"... ({total_lines - limit} more lines)")

        return "\n".join(lines)[:50000]
    except Exception as e:
        return f"Error: {e}"


def run_write(path: str, content: str) -> str:
    """
    Write content to a file, creating parent directories if needed.

    This is for complete file creation/overwrite.
    For partial edits, use Edit tool instead.
    """
    try:
        file_path = safe_path(path)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8", newline="\n")
        return f"Wrote {len(content)} bytes to {path}"
    except Exception as e:
        return f"Error: {e}"


def run_edit(path: str, old_text: str, new_text: str) -> str:
    """
    Replace exact text in a file (surgical edit).

    Uses exact string matching - the old_text must appear verbatim.
    Only replaces the first occurrence to prevent accidental mass changes.
    """
    try:
        file_path = safe_path(path)
        content = file_path.read_text(encoding="utf-8", newline="\n")

        if old_text not in content:
            return f"Error: Text not found in {path}"

        new_content = content.replace(old_text, new_text, 1)
        file_path.write_text(new_content, encoding="utf-8", newline="\n")
        return f"Edited {path}"
    except Exception as e:
        return f"Error: {e}"


def run_task_update(tasks: list[dict[str, str]]) -> str:
    """
    Update the task list.

    The model sends a complete new list (not a diff).
    We validate it and return the renderer view.
    """
    try:
        return task_manager.update(tasks)
    except Exception as e:
        return f"Error: {e}"


def run_task(ctx: "AgentApp", agent_type: str, prompt: str, description: str) -> str:
    """
    Execute a subagent task with isolated context.

    This is the core of the subagent mechanism:

    1. Create isolated message history (KEY: no parent context!)
    2. Use agent-specific system prompt
    3. Filter available tools based on agent type
    4. Run the same query loop as main agent
    5. Return ONLY the final text (not intermediate details)

    The parent agent sees just the summary, keeping its context clean.
    This gives visibility without polluting the main conversation.
    """
    if agent_type not in AGENTS:
        return f"Error: Unknown agent type '{agent_type}'"

    config = AGENTS[agent_type]
    system_prompt = f"""You are a {agent_type} subagent at {WORKDIR}.

{config["prompt"]}

Complete the task and return a clear, concise summary."""
    tools = get_tools_for_agent(agent_type)
    messages: list[MessageParam] = [
        {"role": "user", "content": prompt},
    ]

    tool_count = 0
    interrupted = False
    response = None

    try:
        ctx.output.status(f"Preparing {agent_type} agent...")
        while True:
            response = client.messages.create(
                model=MODEL,
                system=system_prompt,
                messages=messages,
                tools=tools,
                max_tokens=8000,
            )

            if response.stop_reason != "tool_use":
                break

            tool_calls: list[ToolUseBlock] = [
                block for block in response.content if isinstance(block, ToolUseBlock)
            ]
            results: list[ToolResultBlockParam] = []

            for tool_call in tool_calls:
                tool_count += 1
                output = execute_tool(ctx, tool_call.name, tool_call.input)
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": tool_call.id,
                        "content": output,
                    }
                )
                ctx.output.status(f"{get_tool_call_detail(tool_call.name, tool_call.input)}")

            messages.append({"role": "assistant", "content": response.content})
            messages.append({"role": "user", "content": results})

    except KeyboardInterrupt:
        interrupted = True
        ctx.output.interrupted()

    ctx.output.accent(f"  {tool_count} tools used")

    if interrupted:
        return f"(subagent interrupted by user after {tool_count} tool calls)"

    if response is not None:
        for block in response.content:
            if isinstance(block, TextBlock):
                return block.text

    return "(subagent returned no text)"


def run_skill(skill_name: str) -> str:
    """
    Load a skill and inject it into the conversation.

    This is the key mechanism:
    1. Get skill content (SKILL.md body + resource hints)
    2. Return it wrapped in <skill-loaded> tags
    3. Model receives this as tool_result (user message)
    4. Model now "knows" how to do the task
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


def execute_tool(ctx: "AgentApp", name: str, args: dict[str, object]) -> str:
    """
    Dispatch tool call to the appropriate implementation.

    This is the bridge between the model's tool calls and the actual execution.
    Each tool returns a string result that goes back to the model.
    """
    match name:
        case "Bash":
            tool = BashToolCall(name="Bash", command=str(args["command"]))
            return run_bash(tool.command)
        case "Read":
            limit = args.get("limit")
            tool = ReadToolCall(
                name="Read",
                path=str(args["path"]),
                limit=int(limit) if isinstance(limit, (int, float, str)) else None,
            )
            return run_read(tool.path, tool.limit)
        case "Write":
            tool = WriteToolCall(
                name="Write", path=str(args["path"]), content=str(args["content"])
            )
            return run_write(tool.path, tool.content)
        case "Edit":
            tool = EditToolCall(
                name="Edit",
                path=str(args["path"]),
                old_text=str(args["old_text"]),
                new_text=str(args["new_text"]),
            )
            return run_edit(tool.path, tool.old_text, tool.new_text)
        case "TaskUpdate":
            tasks = cast(list[dict[str, str]], args.get("tasks", []))
            tool = TaskUpdateToolCall(name="TaskUpdate", tasks=tasks)
            return run_task_update(tool.tasks)
        case "Task":
            tool = TaskToolCall(
                name="Task",
                agent_type=str(args["agent_type"]),
                prompt=str(args["prompt"]),
                description=str(args["description"]),
            )
            return run_task(ctx, tool.agent_type, tool.prompt, tool.description)
        case "Skill":
            tool = SkillToolCall(name="Skill", skill_name=str(args["skill_name"]))
            return run_skill(tool.skill_name)
        case _:
            return f"Unknown tool: {name}"
