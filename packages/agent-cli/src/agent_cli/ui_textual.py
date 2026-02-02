"""Textual-based UI implementation for agent-cli.

This module provides the TextualOutput class that implements the IAgentUI protocol
using the Textual framework for terminal UI.
"""

from collections.abc import Callable
from pathlib import Path
from typing import cast

from rich.console import RenderableType
from rich.markdown import Markdown
from rich.table import Table
from rich.text import Text
from textual.widgets import RichLog, Static

from .output import get_tool_call_detail, get_tool_result_preview


class TextualOutput:
    """Textual-based implementation of IAgentUI.

    This class decouples UI rendering from the TUI application by using
    callback functions instead of direct references to AgentApp.
    """

    def __init__(
        self,
        get_chat_log: Callable[[], RichLog],
        get_status_bar: Callable[[], Static],
        get_thinking_log: Callable[[], RichLog],
        store_thinking: Callable[[Text], None],
        is_thinking_view: Callable[[], bool],
    ) -> None:
        """Initialize TextualOutput with callback functions.

        Args:
            get_chat_log: Callback to get the main chat RichLog widget.
            get_status_bar: Callback to get the StatusBar widget.
            get_thinking_log: Callback to get the thinking RichLog widget.
            store_thinking: Callback to store formatted thinking content.
            is_thinking_view: Callback to check if currently in thinking view.
        """
        self._get_chat_log = get_chat_log
        self._get_status_bar = get_status_bar
        self._get_thinking_log = get_thinking_log
        self._store_thinking = store_thinking
        self._is_thinking_view = is_thinking_view
        self._chat: RichLog | None = None

    @property
    def chat(self) -> RichLog:
        """Get the chat log widget, caching for performance."""
        if self._chat is None:
            self._chat = self._get_chat_log()
        return self._chat

    def text(self, message: object) -> None:
        """Write a message to the output."""
        self.chat.write(cast(RenderableType, message), animate=True)

    def debug(self, message: str | None) -> None:
        """Write a debug (cyan) styled message."""
        if message is None:
            return
        self.text(Text(message, style="cyan"))

    def newline(self) -> None:
        """Write an empty line."""
        self.text("")

    def clear(self) -> None:
        """Clear the output."""
        if self._chat is None:
            self._chat = self._get_chat_log()
        self._chat.clear()

    def primary(self, message: str | None) -> None:
        """Write a primary (green) styled message."""
        if message is None:
            return
        self.text(Text(message, style="green"))

    def accent(self, message: str | None) -> None:
        """Write an accent (grey) styled message."""
        if message is None:
            return
        self.text(Text(message, style="grey62"))

    def error(self, message: str | None) -> None:
        """Write an error (red) styled message."""
        if message is None:
            return
        self.text(Text(message, style="red"))

    def interrupted(self) -> None:
        """Display interruption message."""
        self.error("\n  ⎿  Interrupted by user")

    def tool_call(self, name: str, tool_input: dict[str, object]) -> None:
        """Display tool call with name and key argument."""
        detail = get_tool_call_detail(name, tool_input)
        self.newline()
        self.text(Text.assemble(("● ", "green"), detail))

    def tool_result(self, output: str | None, max_length: int = 200) -> None:
        """Display tool result preview."""
        preview = get_tool_result_preview(output, max_length)
        self.accent(preview)

    def response(self, text: str | None) -> None:
        """Render model response as Markdown."""
        if text is None:
            return

        self.newline()
        table = Table.grid(padding=0)
        table.add_column(width=2, no_wrap=True)
        table.add_column()
        table.add_row("● ", Markdown(text))
        self.text(table)

    def thinking(self, content: str | None, duration: float | None = None) -> None:
        """Display thinking block indicator with optional duration.

        Thinking content is stored via the callback and can be viewed
        by pressing ctrl+o to toggle thinking view.
        """
        if content is None:
            return

        # Store in thinking history via callback
        formatted = self._format_thinking_block(content)
        self._store_thinking(formatted)

        # Show indicator in main chat
        self.newline()
        duration_str = f"{duration:.1f}s" if duration is not None else ""
        self.text(
            Text.assemble(
                ("∴ ", "blue"),
                (f"Thought for {duration_str}"),
                (" (ctrl+o", "bold dim"),
                (" to view details)", "dim"),
            )
        )

        # If currently in thinking view, update the thinking log
        if self._is_thinking_view():
            self._get_thinking_log().write(formatted)

    def _format_thinking_block(self, content: str) -> Text:
        """Format thinking content with blue bullet and indentation."""
        lines = content.split("\n")
        formatted = Text()
        formatted.append("\n∴ ", style="blue")
        formatted.append(lines[0] if lines else "", style="dim")
        for line in lines[1:]:
            formatted.append("\n  ", style="")  # 2 spaces indent for alignment
            formatted.append(line, style="dim")
        return formatted

    def status(self, message: str | None, spinning: bool = False) -> None:
        """Update the status bar with optional spinner."""
        from .tui import StatusBar

        status_bar = self._get_status_bar()
        if isinstance(status_bar, StatusBar):
            status_bar.update_status(message or "", spinning)
        else:
            status_bar.update(f" {message}")

    def banner(self, model: str, workdir: Path) -> None:
        """Display the startup banner with gradient effect."""
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
