"""Headless UI implementation for agent-cli.

Silent UI that suppresses all intermediate output. Used in headless mode
(`-p/--print`) where only the final response is printed to stdout.
"""

from pathlib import Path


class HeadlessOutput:
    """Silent UI implementation for headless mode.

    All methods are no-ops. The final response is extracted from
    the message history after agent.run() completes.
    """

    # Basic output
    def text(self, message: object) -> None: pass
    def newline(self) -> None: pass
    def clear(self) -> None: pass

    # Styled output
    def primary(self, message: str | None) -> None: pass
    def accent(self, message: str | None) -> None: pass
    def error(self, message: str | None) -> None: pass
    def debug(self, message: str | None) -> None: pass

    # Agent-specific output
    def thinking(self, content: str | None, duration: float | None = None) -> None: pass
    def response(self, text: str | None) -> None: pass
    def tool_call(self, name: str, tool_input: dict[str, object]) -> None: pass
    def tool_result(self, output: str | None, max_length: int = 200) -> None: pass
    def interrupted(self) -> None: pass

    # Status management
    def status(self, message: str | None, spinning: bool = False) -> None: pass
    def banner(self, model: str, workdir: Path) -> None: pass
