from pathlib import Path
from typing import TYPE_CHECKING

from rich.console import RenderableType
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text
from textual.widgets import RichLog

if TYPE_CHECKING:
    from .tui import AgentApp


def get_tool_call_detail(name: str, tool_input: dict[str, object]) -> str:
    """Format tool call detail string."""
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


def get_tool_result_preview(output: str, max_length: int = 200) -> str:
    """Format tool result with prefix and aligned indentation for multi-line output."""
    truncated = output[:max_length] + "..." if len(output) > max_length else output
    return "  ⎿  " + truncated.replace("\n", "\n     ")


class Output:
    """Output abstraction for rendering to the TUI."""

    def __init__(self, app: "AgentApp") -> None:
        self.context = app
        self.chat = None

    def text(self, message: RenderableType) -> None:
        if self.chat is None:
            self.chat = self.context.query_one("#chat", RichLog)
        self.chat.write(message, animate=True)

    def newline(self) -> None:
        self.text("")

    def clear(self) -> None:
        if self.chat is None:
            self.chat = self.context.query_one("#chat", RichLog)
        self.chat.clear()

    def primary(self, message: str) -> None:
        self.text(Text(message, style="green"))

    def accent(self, message: str) -> None:
        self.text(Text(message, style="grey62"))

    def error(self, message: str) -> None:
        self.text(Text(message, style="red"))

    def interrupted(self) -> None:
        self.error("\n  ⎿  Interrupted by user")

    def tool_call(self, name: str, tool_input: dict[str, object]) -> None:
        """Print tool call: ToolName(key_arg)."""
        detail = get_tool_call_detail(name, tool_input)
        self.newline()
        self.text(Text.assemble(("● ", "green"), detail))

    def tool_result(self, output: str, max_length: int = 200) -> None:
        """Print tool result preview in gray."""
        preview = get_tool_result_preview(output, max_length)
        self.accent(preview)

    def response(self, text: str) -> None:
        """Print model text output, rendering Markdown with proper indentation."""
        self.newline()
        table = Table.grid(padding=0)
        table.add_column(width=2, no_wrap=True)
        table.add_column()
        table.add_row("● ", Markdown(text))
        self.text(table)

    def status(self, message: str) -> None:
        """Update the status bar."""
        from .tui import StatusBar

        self.context.query_one("#status", StatusBar).update(message)

    def banner(self, model: str, workdir: Path) -> None:
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

        self.newline()
        for line, color in zip(logo_lines, gradient, strict=False):
            self.text(Text(line, style=f"bold {color}"))
        self.newline()
        self.accent("  ┌─────────────────────────────────────────┐")
        self.accent("  │         AI-Powered Coding Agent         │")
        self.accent("  └─────────────────────────────────────────┘")
        self.newline()
        self.accent(f"  Model:    {model}")
        self.accent(f"  Workdir:  {workdir}")
        self.newline()
        self.text("  Type '/help' to see available commands.")
