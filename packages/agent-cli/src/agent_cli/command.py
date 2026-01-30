from collections.abc import Callable
from typing import Literal

from .llm import MODEL, WORKDIR
from .output import print_accent, print_error, print_newline, print_text
from .skill import skill_loader
from .task import task_manager

type CommandResult = Literal["continue", "exit", "clear"]

# Command registry: command name -> (handler, description)
COMMANDS: dict[str, tuple[Callable[[], CommandResult], str]] = {}


def command(name: str, description: str):
    """Decorator to register a command."""

    def decorator(func: Callable[[], CommandResult]) -> Callable[[], CommandResult]:
        COMMANDS[name] = (func, description)
        return func

    return decorator


@command("/help", "Show available commands")
def cmd_help() -> CommandResult:
    """Display all available commands."""
    print_newline()
    print_accent("  Available commands:")
    for cmd_name, (_, desc) in sorted(COMMANDS.items()):
        print_text(f"  {cmd_name:<12} {desc}")
    print_newline()
    return "continue"


@command("/exit", "Exit the program")
def cmd_exit() -> CommandResult:
    """Exit the program."""
    return "exit"


@command("/clear", "Clear conversation history")
def cmd_clear() -> CommandResult:
    """Clear conversation history and reset state."""
    print_newline()
    print_accent("  Conversation cleared")
    print_newline()
    return "clear"


@command("/skills", "List loaded skills")
def cmd_skills() -> CommandResult:
    """Display all loaded skills."""
    print_newline()
    skills = skill_loader.list_skills()
    if not skills:
        print_accent("  No skills loaded")
    else:
        print_accent(f"  Loaded skills ({len(skills)}):")
        for name in skills:
            skill = skill_loader.skills.get(name)
            if skill:
                tokens = len(name + skill["description"]) // 4
                print_text(f"  {name} · ~{tokens} tokens")

    print_newline()
    return "continue"


@command("/tasks", "Show current task list")
def cmd_tasks() -> CommandResult:
    """Display the current task list."""
    print_newline()
    rendered = task_manager.render()
    for line in rendered.split("\n"):
        print_accent(f"  {line}")
    print_newline()
    return "continue"


@command("/model", "Show model and config info")
def cmd_model() -> CommandResult:
    """Display current model and working directory."""
    print_newline()
    print_accent("  Current configuration:")
    print_text(f"  Model:    {MODEL}")
    print_text(f"  Workdir:  {WORKDIR}")
    print_newline()
    return "continue"


def handle_slash_command(user_input: str) -> CommandResult | None:
    """
    Process user input and handle commands.

    Args:
        user_input: The raw user input string

    Returns:
        - None if input is not a command (doesn't start with /)
        - CommandResult signal for main loop control
    """
    if not user_input.startswith("/"):
        return None

    cmd = user_input.lower().split()[0]

    if cmd in COMMANDS:
        handler, _ = COMMANDS[cmd]
        return handler()

    # Unknown command: show help
    print_newline()
    print_error(f"  Unknown command: {cmd}")
    return cmd_help()
