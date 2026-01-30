from anthropic.types import MessageParam, TextBlockParam

from .command import handle_slash_command
from .context import load_system_reminder
from .llm import MODEL, WORKDIR
from .output import print_banner, print_error, print_newline
from .task import task_manager
from .workflow import agent_loop


def main() -> None:
    print_banner(MODEL, WORKDIR)

    history: list[MessageParam] = []
    first_turn = True

    while True:
        try:
            user_input = input("❯ ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            continue

        result = handle_slash_command(user_input)
        match result:
            case "exit":
                break
            case "clear":
                history.clear()
                first_turn = True
                continue
            case "continue":
                continue
            case _:
                pass

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
            print_error(f"Error: {e}")

        print_newline()
