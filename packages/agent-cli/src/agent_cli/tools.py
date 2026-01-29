import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, cast

from anthropic.types import ToolParam

from .task import TaskManager


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


ToolCall = (
    BashToolCall | ReadToolCall | WriteToolCall | EditToolCall | TaskUpdateToolCall
)


WORKDIR = Path.cwd()

TOOLS: list[ToolParam] = [
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
            },
            "required": ["tasks"],
        },
    },
]


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


def run_task(tasks: list[dict[str, str]]) -> str:
    """
    Update the task list.

    The model sends a complete new list (not a diff).
    We validate it and return the renderer view.
    """
    task_manager = TaskManager()

    try:
        return task_manager.update(tasks)
    except Exception as e:
        return f"Error: {e}"


def execute_tool(name: str, args: dict[str, object]) -> str:
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
            return run_task(tool.tasks)
        case _:
            return f"Unknown tool: {name}"
