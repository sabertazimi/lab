"""Agent type definitions for agent-cli.

This module defines the available agent types for subagent spawning.
"""

from anthropic.types import ToolParam

from .tools import BASE_TOOLS

AGENTS: dict[str, dict[str, str | list[str]]] = {
    # Explore: Read-only agent for searching and analyzing
    # Cannot modify files - safe for broad exploration
    "Explore": {
        "description": "Read-only agent for exploring code, finding files, searching",
        "tools": ["Bash", "Read"],  # No write access
        "prompt": "You are an exploration agent. Search and analyze, but never modify files. Return a concise summary.",
    },
    # Plan: Analysis agent for design work
    # Read-only, focused on producing plans and strategies
    "Plan": {
        "description": "Planning agent for designing implementation strategies",
        "tools": ["Bash", "Read"],  # Read-only
        "prompt": "You are a planning agent. Analyze the codebase and output a numbered implementation plan. Do NOT make changes.",
    },
    # Code: Full-powered agent for implementation
    # Has all tools - use for actual coding work
    "Code": {
        "description": "Full agent for implementing features and fixing bugs",
        "tools": "*",  # All tools
        "prompt": "You are a coding agent. Implement the requested changes efficiently.",
    },
}


def get_agent_description() -> str:
    """Generate agent type descriptions for the Task tool.

    Returns:
        Formatted string of agent type descriptions.
    """
    return "\n".join(
        f"- {name}: {config['description']}" for name, config in AGENTS.items()
    )


def get_tools_for_agent(agent_type: str) -> list[ToolParam]:
    """Filter tools based on agent type.

    Each agent type has a whitelist of allowed tools.
    '*' means all tools (but subagents don't get Task to prevent infinite recursion).

    Args:
        agent_type: The type of agent (Explore, Plan, Code).

    Returns:
        List of allowed tools for the agent type.
    """
    allowed_tools = AGENTS.get(agent_type, {}).get("tools", "*")

    if allowed_tools == "*":
        return BASE_TOOLS

    return [
        tool
        for tool in BASE_TOOLS
        if tool["name"] in allowed_tools  # type: ignore
    ]
