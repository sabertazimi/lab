"""Unit tests for agent-cli skill module."""

from pathlib import Path

import pytest
from agent_cli.skill import SkillLoader


class TestSkillLoader:
    """Tests for SkillLoader class."""

    @pytest.fixture(autouse=True)
    def setup(self, clear_singleton: None) -> None:
        """Ensure fresh SkillLoader for each test."""

    @pytest.fixture
    def skills_dir(self, tmp_path: Path) -> Path:
        """Create a temporary skills directory."""
        skills = tmp_path / "skills"
        skills.mkdir()
        return skills

    @pytest.fixture
    def valid_skill(self, skills_dir: Path) -> Path:
        """Create a valid SKILL.md file."""
        skill_dir = skills_dir / "test-skill"
        skill_dir.mkdir()
        skill_md = skill_dir / "SKILL.md"
        skill_md.write_text(
            "---\nname: test-skill\ndescription: A test skill for unit testing\n---\n\n# Test Skill\n\nThis is the body of the test skill.\n",
            encoding="utf-8",
            newline="\n",
        )
        return skill_md

    def test_parse_skill_valid(self, skills_dir: Path, valid_skill: Path) -> None:
        """parse_skill should extract metadata and body from valid SKILL.md."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))

        skill = loader.parse_skill(valid_skill)

        assert skill is not None
        assert skill["name"] == "test-skill"
        assert skill["description"] == "A test skill for unit testing"
        assert "# Test Skill" in skill["body"]
        assert skill["path"] == valid_skill
        assert skill["dir"] == valid_skill.parent

    def test_parse_skill_no_frontmatter(self, tmp_path: Path) -> None:
        """parse_skill should return None for file without frontmatter."""
        skill_md = tmp_path / "SKILL.md"
        skill_md.write_text("# Just markdown\nNo frontmatter here.", encoding="utf-8")

        loader = SkillLoader(tmp_path, Path("/nonexistent"))
        assert loader.parse_skill(skill_md) is None

    def test_parse_skill_missing_name(self, tmp_path: Path) -> None:
        """parse_skill should return None if name is missing."""
        skill_md = tmp_path / "SKILL.md"
        skill_md.write_text(
            "---\ndescription: Test\n---\nBody",
            encoding="utf-8",
            newline="\n",
        )

        loader = SkillLoader(tmp_path, Path("/nonexistent"))
        assert loader.parse_skill(skill_md) is None

    def test_load_skills_from_dir(self, skills_dir: Path, valid_skill: Path) -> None:
        """load_skills should load valid skills from directory."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))

        assert "test-skill" in loader.skills
        assert loader.skills["test-skill"]["description"] == "A test skill for unit testing"

    def test_load_skills_empty_dir(self, tmp_path: Path) -> None:
        """load_skills should handle empty or nonexistent directory."""
        loader = SkillLoader(tmp_path / "nonexistent", Path("/nonexistent"))
        assert loader.skills == {}

    def test_get_descriptions(self, skills_dir: Path, valid_skill: Path) -> None:
        """get_descriptions should return formatted skill list."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))

        result = loader.get_descriptions()

        assert "test-skill" in result
        assert "A test skill for unit testing" in result

    def test_get_descriptions_empty(self, tmp_path: Path) -> None:
        """get_descriptions should return placeholder when no skills."""
        loader = SkillLoader(tmp_path / "nonexistent", Path("/nonexistent"))
        assert loader.get_descriptions() == "(no skills available)"

    def test_get_skill_found(self, skills_dir: Path, valid_skill: Path) -> None:
        """get_skill should return full content for existing skill."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))

        result = loader.get_skill("test-skill")

        assert result is not None
        assert "# Skill: test-skill" in result
        assert "# Test Skill" in result

    def test_get_skill_not_found(self, skills_dir: Path) -> None:
        """get_skill should return None for nonexistent skill."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))
        assert loader.get_skill("nonexistent") is None

    def test_get_skill_with_resources(self, skills_dir: Path, valid_skill: Path) -> None:
        """get_skill should list available resources."""
        # Create resource directories
        skill_dir = valid_skill.parent
        scripts_dir = skill_dir / "scripts"
        scripts_dir.mkdir()
        (scripts_dir / "setup.sh").write_text("#!/bin/bash", encoding="utf-8")

        loader = SkillLoader(skills_dir, Path("/nonexistent"))
        result = loader.get_skill("test-skill")

        assert result is not None
        assert "Available Resources" in result
        assert "Scripts" in result
        assert "setup.sh" in result

    def test_list_skills(self, skills_dir: Path, valid_skill: Path) -> None:
        """list_skills should return list of skill names."""
        loader = SkillLoader(skills_dir, Path("/nonexistent"))
        assert loader.list_skills() == ["test-skill"]

    def test_list_skills_empty(self, tmp_path: Path) -> None:
        """list_skills should return empty list when no skills."""
        loader = SkillLoader(tmp_path / "nonexistent", Path("/nonexistent"))
        assert loader.list_skills() == []
