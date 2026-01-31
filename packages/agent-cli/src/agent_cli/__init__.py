from .tui import AgentApp


def main() -> None:
    """Entry point for TUI mode."""
    app = AgentApp()
    app.run()
