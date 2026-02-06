import argparse


def main() -> None:
    """Entry point for agent-cli."""
    parser = argparse.ArgumentParser(
        prog="ac",
        description="Cyber Code - AI-Powered Coding Agent",
    )
    parser.add_argument(
        "-p",
        "--print",
        dest="prompt",
        type=str,
        default=None,
        help="Run in headless mode: execute the prompt and print the response to stdout",
    )
    args = parser.parse_args()

    if args.prompt is not None:
        from .headless import HeadlessApp

        app = HeadlessApp()
        app.run(args.prompt)
    else:
        from .tui import AgentApp

        app = AgentApp()
        app.run()
