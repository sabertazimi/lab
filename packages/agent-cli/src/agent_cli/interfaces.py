"""Interface definitions for agent-cli.

This module defines the Protocol interfaces that enable loose coupling
between the Agent core and UI implementations.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from .skill import SkillLoader


@runtime_checkable
class IAgentUI(Protocol):
    """UI output interface that all UI implementations must implement.

    This protocol defines the contract for outputting information to the user.
    Any class implementing this protocol can be used as the UI layer for the Agent.
    """

    # Basic output
    def text(self, message: object) -> None:  # RenderableType is covariant
        """Write a message to the output."""
        ...

    def newline(self) -> None:
        """Write an empty line."""
        ...

    def clear(self) -> None:
        """Clear the output."""
        ...

    # Styled output
    def primary(self, message: str | None) -> None:
        """Write a primary (green) styled message."""
        ...

    def accent(self, message: str | None) -> None:
        """Write an accent (grey) styled message."""
        ...

    def error(self, message: str | None) -> None:
        """Write an error (red) styled message."""
        ...

    def debug(self, message: str | None) -> None:
        """Write a debug (cyan) styled message."""
        ...

    # Agent-specific output
    def thinking(self, content: str | None, duration: float | None = None) -> None:
        """Display thinking block indicator with optional duration."""
        ...

    def response(self, text: str | None) -> None:
        """Render model response as Markdown."""
        ...

    def tool_call(self, name: str, tool_input: dict[str, object]) -> None:
        """Display tool call with name and key argument."""
        ...

    def tool_result(self, output: str | None, max_length: int = 200) -> None:
        """Display tool result preview."""
        ...

    def interrupted(self) -> None:
        """Display interruption message."""
        ...

    # Status management
    def status(self, message: str | None) -> None:
        """Update the status bar."""
        ...

    def banner(self, model: str, workdir: Path) -> None:
        """Display the startup banner."""
        ...


@runtime_checkable
class ICommandContext(Protocol):
    """Command handler context interface.

    This protocol defines the context available to slash command handlers.
    It provides access to the UI and application state without coupling
    to specific implementations.
    """

    @property
    def ui(self) -> IAgentUI:
        """Get the UI output interface."""
        ...

    def clear_history(self) -> None:
        """Clear conversation history and reset state."""
        ...

    def get_model(self) -> str:
        """Get the current model name."""
        ...

    def get_workdir(self) -> Path:
        """Get the current working directory."""
        ...

    def get_skill_loader(self) -> SkillLoader:
        """Get the skill loader instance."""
        ...
