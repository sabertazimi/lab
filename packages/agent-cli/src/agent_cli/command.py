from collections.abc import Callable
from typing import TYPE_CHECKING, Literal

from .llm import MODEL, WORKDIR
from .skill import skill_loader

if TYPE_CHECKING:
    from .tui import AgentApp

type CommandResult = Literal["continue", "exit", "clear"]
type CommandHandler = Callable[["AgentApp"], CommandResult]

# Command registry: command name -> (handler, description)
COMMANDS: dict[str, tuple[CommandHandler, str]] = {}


def command(name: str, description: str):
    """Decorator to register a command."""

    def decorator(func: CommandHandler) -> CommandHandler:
        COMMANDS[name] = (func, description)
        return func

    return decorator


@command("/help", "Show available commands")
def cmd_help(ctx: "AgentApp") -> CommandResult:
    """Display all available commands."""
    ctx.output.newline()
    ctx.output.accent("  Available commands:")
    for cmd_name, (_, desc) in sorted(COMMANDS.items()):
        ctx.output.text(f"  {cmd_name:<12} {desc}")
    ctx.output.newline()
    return "continue"


@command("/exit", "[bold green](Ctrl+W)[/] Exit the program")
def cmd_exit(ctx: "AgentApp") -> CommandResult:
    """Exit the program."""
    return "exit"


@command("/clear", "Clear conversation history")
def cmd_clear(ctx: "AgentApp") -> CommandResult:
    """Clear conversation history and reset state."""
    ctx.output.newline()
    ctx.output.accent("  Conversation cleared")
    ctx.output.newline()
    return "clear"


@command("/skills", "List loaded skills")
def cmd_skills(ctx: "AgentApp") -> CommandResult:
    """Display all loaded skills."""
    ctx.output.newline()
    skills = skill_loader.list_skills()
    if not skills:
        ctx.output.accent("  No skills loaded")
    else:
        ctx.output.accent(f"  Loaded skills ({len(skills)}):")
        for name in skills:
            skill = skill_loader.skills.get(name)
            if skill:
                tokens = len(name + skill["description"]) // 4
                ctx.output.text(f"  {name} · ~{tokens} tokens")

    ctx.output.newline()
    return "continue"


@command("/config", "Show config info")
def cmd_config(ctx: "AgentApp") -> CommandResult:
    """Display current model and working directory."""
    ctx.output.newline()
    ctx.output.accent("  Current configuration:")
    ctx.output.text(f"  Model:    {MODEL}")
    ctx.output.text(f"  Workdir:  {WORKDIR}")
    ctx.output.newline()
    return "continue"


def handle_slash_command(ctx: "AgentApp", user_input: str) -> CommandResult | None:
    """
    Process user input and handle commands.

    Args:
        ctx: The AgentApp instance
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
        return handler(ctx)

    # Unknown command: show help
    ctx.output.newline()
    ctx.output.error(f"  Unknown command: {cmd}")
    return cmd_help(ctx)
