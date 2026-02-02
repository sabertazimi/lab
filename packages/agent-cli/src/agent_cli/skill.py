"""Skill system for agent-cli.

This module provides the SkillLoader class for loading and managing skills
from SKILL.md files. The singleton pattern has been removed to support
dependency injection.
"""

import json
import re
from pathlib import Path
from typing import TypedDict


class Skill(TypedDict):
    """Skill definition loaded from SKILL.md."""

    name: str
    description: str
    body: str
    path: Path
    dir: Path


class SkillLoader:
    """Loads and manages skills from SKILL.md files.

    The YAML frontmatter provides metadata (name, description).
    The markdown body provides detailed instructions.

    Attributes:
        skills_dir: Directory for local skills.
        plugins_dir: Directory for Claude Code Plugins.
        skills: Dictionary of loaded skills.
    """

    def __init__(self, workdir: Path, plugins_dir: Path | None = None) -> None:
        """Initialize the skill loader.

        Args:
            workdir: Working directory. Skills are loaded from {workdir}/.claude/skills.
            plugins_dir: Claude Code Plugins directory (default: ~/.claude/plugins).
        """
        self.skills_dir = workdir / ".claude" / "skills"
        self.plugins_dir = plugins_dir or Path.home() / ".claude" / "plugins"
        self.skills: dict[str, Skill] = {}
        self.load_skills()

    def parse_skill(self, path: Path) -> Skill | None:
        """Parse a SKILL.md file into metadata and body.

        Args:
            path: Path to the SKILL.md file.

        Returns:
            Skill dict with name, description, body, path, dir.
            None if file doesn't match expected format.
        """
        content = path.read_text(encoding="utf-8", newline="\n")

        match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
        if not match:
            return None

        frontmatter, body = match.groups()

        metadata = {}
        for line in frontmatter.strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().strip("\"'")

        if "name" not in metadata or "description" not in metadata:
            return None

        return {
            "name": metadata["name"],
            "description": metadata["description"],
            "body": body.strip(),
            "path": path,
            "dir": path.parent,
        }

    def load_skills(self) -> None:
        """Load skills from local directory and Claude Code Plugins.

        Local skills are loaded first and have priority over plugin skills.
        Only loads metadata at startup - body is loaded on-demand.
        This keeps the initial context lean.
        """
        self._load_skills_from_dir(self.skills_dir)
        self._load_plugin_skills()

    def _load_skills_from_dir(self, skills_dir: Path) -> None:
        """Scan a skills directory and load all valid SKILL.md files.

        Won't override existing skills with the same name.

        Args:
            skills_dir: Directory to scan for skills.
        """
        if not skills_dir.exists():
            return

        for skill_dir in skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue

            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue

            skill = self.parse_skill(skill_md)
            if skill and skill["name"] not in self.skills:
                self.skills[skill["name"]] = skill

    def _load_plugin_skills(self) -> None:
        """Load skills from Claude Code Plugins.

        Reads installed_plugins.json to find plugin install paths,
        then loads skills from each plugin's skills directory.
        """
        installed_plugins = self.plugins_dir / "installed_plugins.json"
        if not installed_plugins.exists():
            return

        try:
            data = json.loads(installed_plugins.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return

        for plugin_entries in data.get("plugins", {}).values():
            for entry in plugin_entries:
                install_path = entry.get("installPath", "")
                if not install_path:
                    continue
                skills_dir = Path(install_path) / "skills"
                self._load_skills_from_dir(skills_dir)

    def get_descriptions(self) -> str:
        """Generate skill descriptions for system prompt.

        This is Layer 1 - only name and description, ~100 tokens per skill.
        Full content (Layer 2) is loaded only when Skill tool is called.

        Returns:
            Formatted string of skill descriptions.
        """
        if not self.skills:
            return "(no skills available)"

        return "\n".join(
            f"- {name}: {skill['description']}" for name, skill in self.skills.items()
        )

    def get_skill(self, name: str) -> str | None:
        """Get full skill content for injection.

        This is Layer 2 - the complete SKILL.md body, plus any available
        resources (Layer 3 hints).

        Args:
            name: Skill name to load.

        Returns:
            Full skill content, or None if skill not found.
        """
        if name not in self.skills:
            return None

        skill = self.skills[name]
        if skill["body"].startswith("# "):
            content = skill["body"]
        else:
            content = f"# Skill: {skill['name']}\n\n{skill['body']}"

        # Layer 3 hints: list available resources in skill directory
        resources: list[str] = []
        for folder, label in [
            ("scripts", "Scripts"),
            ("references", "References"),
            ("examples", "Examples"),
            ("assets", "Assets"),
        ]:
            folder_path = skill["dir"] / folder
            if folder_path.exists():
                files = list(folder_path.glob("*"))
                if files:
                    resources.append(
                        f"- {label}: {', '.join(file.name for file in files)}"
                    )

        if resources:
            content += f"\n\n## Available Resources\n{'\n'.join(resources)}"

        return content

    def list_skills(self) -> list[str]:
        """Return list of available skill names.

        Returns:
            List of skill names.
        """
        return list(self.skills.keys())
