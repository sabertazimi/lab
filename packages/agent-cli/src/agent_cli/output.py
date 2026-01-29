from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from .task import task_manager

console = Console()


def print_text(text: str) -> None:
    """Print model text output with bullet prefix, rendering Markdown."""
    console.print()
    table = Table.grid(padding=0)
    table.add_column(width=2, no_wrap=True)
    table.add_column()
    table.add_row("● ", Markdown(text))
    console.print(table)


def print_tool_call(name: str, tool_input: dict[str, object]) -> None:
    """Print tool call: ToolName(key_arg)."""
    console.print("\n", end="")
    console.print("● ", style="green", end="")
    console.print(get_tool_call_detail(name, tool_input))


def print_tool_result(output: str, max_length: int = 200) -> None:
    """Print tool result preview in gray."""
    preview_text = output[:max_length] + "..." if len(output) > max_length else output
    table = Table.grid(padding=0)
    table.add_column(width=5, no_wrap=True)
    table.add_column()
    table.add_row("  ⎿  ", preview_text)
    console.print(table, style="bright_black")


def get_tool_call_detail(name: str, tool_input: dict[str, object]) -> str:
    match name:
        case "Bash":
            detail = str(tool_input.get("command", ""))
        case "Read":
            detail = str(tool_input.get("path", ""))
        case "Write":
            detail = str(tool_input.get("path", ""))
        case "Edit":
            detail = str(tool_input.get("path", ""))
        case "TaskUpdate":
            if task_manager.total_count == 0:
                detail = "🚀"
            elif task_manager.completed_count + 1 == task_manager.total_count:
                detail = "🏁"
            else:
                detail = (
                    f"{task_manager.completed_count + 1}/{task_manager.total_count}"
                )
        case "Task":
            detail = str(tool_input.get("description", ""))
        case "Skill":
            detail = str(tool_input.get("skill_name", ""))
        case _:
            detail = str(tool_input)
    return f"{name}({detail})"
