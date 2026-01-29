from pathlib import Path

from anthropic.types import MessageParam, TextBlockParam

from .agent import agent_loop
from .task import TaskManager

WORKDIR = Path.cwd()


def main() -> None:
    print(f"Minimal Claude Code - {WORKDIR}")
    print("Type '/exit' to quit.\n")

    history: list[MessageParam] = []
    first_turn = True

    while True:
        try:
            user_input = input("❯ ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            continue
        if user_input.lower() == "/exit":
            break

        content: list[TextBlockParam] = []

        if first_turn:
            content.append({"type": "text", "text": TaskManager.INITIAL_REMINDER})
            first_turn = False

        content.append({"type": "text", "text": user_input})
        history.append({"role": "user", "content": content})

        try:
            agent_loop(history)
        except Exception as e:
            print(f"Error: {e}")

        print()
