from rich.markdown import Markdown
from rich.table import Table

from .console import console
from .llm import MODEL, WORKDIR


def print_banner() -> None:
    """Print ASCII art banner with gradient effect."""
    logo_lines = [
        r"   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ",
        r"  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗",
        r"  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝",
        r"  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗",
        r"  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║",
        r"   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝",
        r"      ██████╗ ██████╗ ██████╗ ███████╗     ",
        r"     ██╔════╝██╔═══██╗██╔══██╗██╔════╝     ",
        r"     ██║     ██║   ██║██║  ██║█████╗       ",
        r"     ██║     ██║   ██║██║  ██║██╔══╝       ",
        r"     ╚██████╗╚██████╔╝██████╔╝███████╗     ",
        r"      ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝     ",
    ]

    # Gradient colors: cyan -> blue -> magenta
    base_colors = [
        "bright_cyan",
        "cyan",
        "dodger_blue2",
        "dodger_blue1",
        "blue_violet",
        "medium_purple1",
    ]
    repeats = (len(logo_lines) + len(base_colors) - 1) // len(base_colors)
    gradient = (base_colors * repeats)[: len(logo_lines)]

    console.print()
    for line, color in zip(logo_lines, gradient, strict=False):
        console.print(line, style=f"bold {color}")

    console.print()
    console.print("  ┌─────────────────────────────────────────┐", style="accent")
    console.print("  │         AI-Powered Coding Agent         │", style="accent")
    console.print("  └─────────────────────────────────────────┘", style="accent")
    console.print()

    console.print(f"  {MODEL}", style="accent")
    console.print(f"  {WORKDIR}", style="accent")
    console.print()
    console.print("  Type '/exit' to quit.\n")


def print_text(text: str) -> None:
    """Print model text output with bullet prefix, rendering Markdown."""
    console.print()
    table = Table.grid(padding=0)
    table.add_column(width=2, no_wrap=True)
    table.add_column()
    table.add_row("● ", Markdown(text))
    console.print(table)


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
            detail = str(tool_input.get("description", ""))
        case "Task":
            detail = str(tool_input.get("description", ""))
        case "Skill":
            detail = str(tool_input.get("skill_name", ""))
        case _:
            detail = str(tool_input)
    return f"{name}({detail})"


def print_tool_call(name: str, tool_input: dict[str, object]) -> None:
    """Print tool call: ToolName(key_arg)."""
    console.print("\n", end="")
    console.print("● ", style="primary", end="")
    console.print(get_tool_call_detail(name, tool_input))


def get_tool_result_preview(output: str, max_length: int = 200) -> str:
    """Format tool result with prefix and aligned indentation for multi-line output."""
    truncated = output[:max_length] + " ..." if len(output) > max_length else output
    return "  ⎿  " + truncated.replace("\n", "\n     ")


def print_tool_result(output: str, max_length: int = 200) -> None:
    """Print tool result preview in gray."""
    console.print(get_tool_result_preview(output, max_length), style="accent")
