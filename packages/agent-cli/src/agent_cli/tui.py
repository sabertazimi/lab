"""Textual TUI for agent-cli.

This module provides the main TUI application that assembles all components
and implements the ICommandContext interface.
"""

from pathlib import Path

from rich.text import Text
from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.geometry import Offset
from textual.widgets import Footer, Input, RichLog, Static
from textual_autocomplete import AutoComplete, DropdownItem, TargetState

from .agent import Agent
from .command import COMMANDS, handle_slash_command
from .config import AgentConfig
from .skill import SkillLoader
from .system import build_system_prompt
from .task import TaskManager
from .tools import build_all_tools
from .ui_textual import TextualOutput


class CommandAutoComplete(AutoComplete):
    """AutoComplete that opens upward for bottom-docked Input."""

    def _align_to_target(self) -> None:
        """Align dropdown above the target cursor position."""
        x, y = self.target.cursor_screen_offset
        dropdown = self.option_list
        _width, height = dropdown.outer_size
        # Position above the input: y - height instead of y + 1
        self.absolute_offset = Offset(x - 1, y - height)


class StatusBar(Static):
    """Status bar widget showing current state."""


class AgentApp(App[None]):
    """Main TUI application for agent-cli.

    Implements ICommandContext interface for slash commands.
    """

    CSS_PATH = "tui.tcss"

    BINDINGS = [
        Binding("ctrl+c", "interrupt", "Interrupt", priority=True),
        Binding("ctrl+l", "clear", "Clear Screen"),
        Binding("ctrl+o", "toggle_thinking", "Thinking View"),
        Binding("ctrl+q", "none", "No Operation", show=False),
        Binding("ctrl+w", "quit", "Quit", priority=True),
    ]

    def __init__(self) -> None:
        super().__init__()

        # Load configuration
        self.config = AgentConfig.from_settings()

        # Initialize dependencies (non-singleton)
        self.skill_loader = SkillLoader(self.config.workdir)
        self.task_manager = TaskManager()

        # UI output (lazy initialization)
        self._output: TextualOutput | None = None

        # Agent (lazy initialization)
        self._agent: Agent | None = None

        # State
        self.thinking_history: list[Text] = []
        self.show_thinking = False
        self._is_running = False

    # ICommandContext implementation
    @property
    def ui(self) -> TextualOutput:
        """Get the UI output interface."""
        return self.output

    def clear_history(self) -> None:
        """Clear conversation history and reset state."""
        self._agent = self._create_agent()
        self.thinking_history.clear()

    def get_model(self) -> str:
        """Get the current model name."""
        return self.config.model

    def get_workdir(self) -> Path:
        """Get the current working directory."""
        return self.config.workdir

    def get_skill_loader(self) -> SkillLoader:
        """Get the skill loader instance."""
        return self.skill_loader

    @property
    def output(self) -> TextualOutput:
        """Get or create the TextualOutput instance."""
        if self._output is None:
            self._output = TextualOutput(
                get_chat_log=lambda: self.query_one("#chat", RichLog),
                get_status_bar=lambda: self.query_one("#status", StatusBar),
                get_thinking_log=lambda: self.query_one("#thinking", RichLog),
                store_thinking=lambda t: self.thinking_history.append(t),
                is_thinking_view=lambda: self.show_thinking,
            )
        return self._output

    def _create_agent(self) -> Agent:
        """Create a new Agent instance."""
        system_prompt = build_system_prompt(
            self.config.workdir,
            self.skill_loader,
        )
        return Agent(
            ui=self.output,
            config=self.config,
            system_prompt=system_prompt,
            tools=build_all_tools(self.skill_loader),
            skill_loader=self.skill_loader,
            task_manager=self.task_manager,
        )

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield RichLog(id="chat", highlight=True, markup=True, wrap=True)
        yield RichLog(
            id="thinking", highlight=True, markup=True, wrap=True, classes="hidden"
        )
        yield StatusBar("", id="status")
        input_widget = Input(
            placeholder="Type a message or /help for commands...", id="input"
        )
        yield input_widget
        yield CommandAutoComplete(input_widget, candidates=self._get_command_candidates)
        yield Footer()

    def _get_command_candidates(self, state: TargetState) -> list[DropdownItem]:
        """Return slash command candidates when input starts with /"""
        if not state.text.startswith("/"):
            return []
        return [DropdownItem(main=cmd[0]) for cmd in sorted(COMMANDS.items())]

    def on_mount(self) -> None:
        """Called when app is mounted."""
        # Report any config errors
        self.config.report_errors(self.output)

        # Show banner
        self.output.banner(self.config.model, self.config.workdir)

        # Create agent
        self._agent = self._create_agent()

        # Focus input
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
                "\n  [yellow]Agent is still running. Press ctrl+c to interrupt.[/]"
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
                    self.clear_history()
                    self.output.clear()
                    self.output.banner(self.config.model, self.config.workdir)
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
            assert self._agent is not None
            self._agent.run(user_input)

        except Exception as e:
            self.call_from_thread(self.output.error, f"Error: {e}")

        finally:
            self._is_running = False
            self.call_from_thread(self.output.status, "Ready")

    def action_interrupt(self) -> None:
        """ctrl+c: interrupt agent loop"""
        if self._is_running and self._agent is not None:
            self.output.status("Interrupting...")
            self._agent.request_interrupt()

    def action_clear(self) -> None:
        """ctrl+l: clear terminal screen"""
        self.output.clear()
        self.output.banner(self.config.model, self.config.workdir)

    def action_toggle_thinking(self) -> None:
        """ctrl+o: toggle thinking view"""
        chat_log = self.query_one("#chat", RichLog)
        thinking_log = self.query_one("#thinking", RichLog)

        self.show_thinking = not self.show_thinking

        if self.show_thinking:
            # Switch to thinking view
            chat_log.add_class("hidden")
            thinking_log.remove_class("hidden")
            thinking_log.clear()
            if self.thinking_history:
                for thinking in self.thinking_history:
                    thinking_log.write(thinking)
            else:
                thinking_log.write("[dim]No thinking content yet.[/]")
            self.output.status("Thinking View (ctrl+o to return)")
        else:
            # Switch back to chat view
            thinking_log.add_class("hidden")
            chat_log.remove_class("hidden")
            self.output.status("Ready" if not self._is_running else "Thinking...")
