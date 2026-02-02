"""Output utilities for agent-cli.

This module contains utility functions for formatting tool calls and results.
The actual UI implementation has been moved to ui_textual.py.
"""


def get_tool_call_detail(name: str, tool_input: dict[str, object]) -> str:
    """Format tool call detail string.

    Args:
        name: Tool name.
        tool_input: Tool input arguments.

    Returns:
        Formatted string like "ToolName(key_arg)".
    """
    match name:
        case "Bash":
            detail = str(tool_input.get("command", ""))
        case "Read":
            detail = str(tool_input.get("path", ""))
        case "Write":
            detail = str(tool_input.get("path", ""))
        case "Edit":
            detail = str(tool_input.get("path", ""))
        case "Glob":
            detail = str(tool_input.get("pattern", ""))
        case "Grep":
            detail = str(tool_input.get("pattern", ""))
        case "WebSearch":
            detail = str(tool_input.get("query", ""))
        case "WebReader":
            detail = str(tool_input.get("url", ""))
        case "TaskUpdate":
            detail = str(tool_input.get("list_title", ""))
        case "Task":
            detail = str(tool_input.get("description", ""))
        case "Skill":
            detail = str(tool_input.get("skill_name", ""))
        case _:
            detail = str(tool_input)
    return f"{name}({detail})"


def get_tool_result_preview(output: str | None, max_length: int = 200) -> str:
    """Format tool result with prefix and aligned indentation for multi-line output.

    Args:
        output: Tool output string.
        max_length: Maximum length before truncation (default: 200).

    Returns:
        Formatted preview string with indentation.
    """
    if output is None:
        return "Empty"

    truncated = output[:max_length] + "..." if len(output) > max_length else output
    truncated = truncated.strip()
    return "  ⎿  " + truncated.replace("\n", "\n     ")
