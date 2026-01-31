"""Textual TUI for agent-cli."""

from anthropic.types import MessageParam, TextBlockParam
from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Input, RichLog, Static

from .command import handle_slash_command
from .context import load_system_reminder
from .llm import MODEL, WORKDIR, report_config_errors
from .output import Output
from .task import task_manager
from .workflow import agent_loop, request_interrupt


class StatusBar(Static):
    """Status bar widget showing current state."""

    DEFAULT_CSS = """
    StatusBar {
        height: 1;
        background: $surface;
        color: $text-muted;
        padding: 0 1;
        border-top: solid $primary;
    }
    """


class AgentApp(App[None]):
    """Main TUI application for agent-cli."""

    CSS = """
    Screen {
        layout: vertical;
    }

    RichLog {
        height: 1fr;
        scrollbar-gutter: stable;
    }

    StatusBar {
        height: 1;
    }

    Input {
        dock: bottom;
    }
    """

    BINDINGS = [
        Binding("ctrl+c", "interrupt", "Interrupt"),
        Binding("ctrl+l", "clear", "Clear"),
        Binding("ctrl+q", "none", "No Operation", show=False),
        Binding("ctrl+w", "quit", "Quit", priority=True),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.output = Output(self)
        self.history: list[MessageParam] = []
        self.first_turn = True
        self._is_running = False

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield RichLog(id="chat", highlight=True, markup=True, wrap=True)
        yield StatusBar("Ready", id="status")
        yield Input(placeholder="Type a message or /help for commands...", id="input")
        yield Footer()

    def on_mount(self) -> None:
        """Called when app is mounted."""
        report_config_errors(self)
        self.output.banner(MODEL, WORKDIR)
        self.query_one("#input", Input).focus()

    @on(Input.Submitted)
    async def on_input_submit(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        user_input = event.value.strip()
        if not user_input:
            return

        event.input.clear()

        # Don't accept new input while agent is running
        if self._is_running:
            self.output.text(
                "[yellow]Agent is still running. Press Ctrl+C to interrupt.[/]"
            )
            return

        # Show user input
        self.output.newline()
        self.output.text(f"[bold green]❯[/] {user_input}")

        # Handle slash commands
        result = handle_slash_command(self, user_input)
        if result is not None:
            match result:
                case "exit":
                    self.exit(return_code=0)
                case "clear":
                    self.history.clear()
                    self.first_turn = True
                    self.output.clear()
                    self.output.banner(MODEL, WORKDIR)
                case "continue":
                    pass
            return

        # Run agent in background worker
        self.run_agent(user_input)

    @work(exclusive=True, thread=True)
    def run_agent(self, user_input: str) -> None:
        """Run agent loop in a background thread."""
        self._is_running = True
        self.call_from_thread(self.output.status, "Thinking...")

        try:
            # Build message content
            content: list[TextBlockParam] = []

            if self.first_turn:
                system_reminder = load_system_reminder(WORKDIR)
                if system_reminder:
                    content.append({"type": "text", "text": system_reminder})
                content.append({"type": "text", "text": task_manager.INITIAL_REMINDER})
                self.first_turn = False

            content.append({"type": "text", "text": user_input})
            self.history.append({"role": "user", "content": content})

            # Run agent loop
            agent_loop(self, self.history)

        except Exception as e:
            self.call_from_thread(self.output.error, f"Error: {e}")

        finally:
            self._is_running = False
            self.call_from_thread(self.output.status, "Ready")

    def action_interrupt(self) -> None:
        """Handle interrupt action (Ctrl+C key)."""
        if self._is_running:
            request_interrupt()
            self.output.status("Interrupting...")

    def action_clear(self) -> None:
        """Handle clear action (Ctrl+L key)."""
        self.output.clear()
        self.output.banner(MODEL, WORKDIR)
