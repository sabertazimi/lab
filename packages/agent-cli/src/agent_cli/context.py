from pathlib import Path


def load_system_reminder(workdir: Path) -> str | None:
    """
    Load CLAUDE.md from workdir and format as system-reminder message.

    Args:
        workdir: The working directory to search for CLAUDE.md

    Returns:
        Formatted system-reminder string, or None if file doesn't exist
    """
    claude_md = workdir / "CLAUDE.md"
    if not claude_md.exists():
        return None

    try:
        content = claude_md.read_text(encoding="utf-8", newline="\n")
    except (OSError, UnicodeError):
        return None
    return f"""<system-reminder>
Below are the project-specific guidelines from the CLAUDE.md file:
{content}
</system-reminder>"""
