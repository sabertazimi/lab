from anthropic.types import MessageParam, TextBlockParam

from .console import console
from .context import load_system_reminder
from .llm import WORKDIR
from .output import print_banner
from .task import task_manager
from .workflow import agent_loop


def main() -> None:
    print_banner()

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
            system_reminder = load_system_reminder(WORKDIR)
            if system_reminder:
                content.append({"type": "text", "text": system_reminder})
            content.append({"type": "text", "text": task_manager.INITIAL_REMINDER})
            first_turn = False

        content.append({"type": "text", "text": user_input})
        history.append({"role": "user", "content": content})

        try:
            agent_loop(history)
        except Exception as e:
            console.print(f"Error: {e}", style="error")

        console.print()
