"""Slash command system for agent-cli.

This module provides the command registry and handlers for slash commands.
Commands use the ICommandContext interface instead of direct AgentApp reference.
"""

from collections.abc import Callable
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from .interfaces import ICommandContext

type CommandResult = Literal["continue", "exit", "clear"]
type CommandHandler = Callable[["ICommandContext"], CommandResult]

# Command registry: command name -> (handler, description)
COMMANDS: dict[str, tuple[CommandHandler, str]] = {}


def command(name: str, description: str):
    """Decorator to register a command.

    Args:
        name: Command name (e.g., "/help").
        description: Command description for help display.
    """

    def decorator(func: CommandHandler) -> CommandHandler:
        COMMANDS[name] = (func, description)
        return func

    return decorator


@command("/help", "Show available commands")
def cmd_help(ctx: ICommandContext) -> CommandResult:
    """Display all available commands."""
    ctx.ui.newline()
    ctx.ui.accent("  Available commands:")
    for cmd_name, (_, desc) in sorted(COMMANDS.items()):
        ctx.ui.text(f"  {cmd_name:<12} {desc}")
    ctx.ui.newline()
    return "continue"


@command("/exit", "[bold green](ctrl+w)[/] Exit the program")
def cmd_exit(ctx: ICommandContext) -> CommandResult:
    """Exit the program."""
    return "exit"


@command("/clear", "Clear conversation history")
def cmd_clear(ctx: ICommandContext) -> CommandResult:
    """Clear conversation history and reset state."""
    ctx.ui.newline()
    ctx.ui.accent("  Conversation cleared")
    ctx.ui.newline()
    return "clear"


@command("/skills", "List loaded skills")
def cmd_skills(ctx: ICommandContext) -> CommandResult:
    """Display all loaded skills."""
    ctx.ui.newline()
    skill_loader = ctx.get_skill_loader()
    skills = skill_loader.list_skills()
    if not skills:
        ctx.ui.accent("  No skills loaded")
    else:
        ctx.ui.accent(f"  Loaded skills ({len(skills)}):")
        for name in skills:
            skill = skill_loader.skills.get(name)
            if skill:
                tokens = len(name + skill["description"]) // 4
                ctx.ui.text(f"  {name} · ~{tokens} tokens")

    ctx.ui.newline()
    return "continue"


@command("/config", "Show config info")
def cmd_config(ctx: ICommandContext) -> CommandResult:
    """Display current model and working directory."""
    ctx.ui.newline()
    ctx.ui.accent("  Current configuration:")
    ctx.ui.text(f"  Model:    {ctx.get_model()}")
    ctx.ui.text(f"  Workdir:  {ctx.get_workdir()}")
    ctx.ui.newline()
    return "continue"


def handle_slash_command(ctx: ICommandContext, user_input: str) -> CommandResult | None:
    """Process user input and handle commands.

    Args:
        ctx: The command context implementing ICommandContext.
        user_input: The raw user input string.

    Returns:
        None if input is not a command (doesn't start with /).
        CommandResult signal for main loop control otherwise.
    """
    if not user_input.startswith("/"):
        return None

    cmd = user_input.lower().split()[0]

    if cmd in COMMANDS:
        handler, _ = COMMANDS[cmd]
        return handler(ctx)

    # Unknown command: show help
    ctx.ui.newline()
    ctx.ui.error(f"  Unknown command: {cmd}")
    return cmd_help(ctx)
