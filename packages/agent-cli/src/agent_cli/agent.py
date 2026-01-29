AGENTS = {
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
    """Generate agent type descriptions for the Task tool."""
    return "\n".join(
        f"- {name}: {config['description']}" for name, config in AGENTS.items()
    )
