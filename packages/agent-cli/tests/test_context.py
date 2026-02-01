"""Unit tests for agent-cli context module."""

from pathlib import Path

from agent_cli.context import load_system_reminder


class TestLoadSystemReminder:
    """Tests for load_system_reminder() function."""

    def test_load_existing_file(self, tmp_path: Path) -> None:
        """Should return formatted content when CLAUDE.md exists."""
        claude_md = tmp_path / "CLAUDE.md"
        claude_md.write_text("# Project Guidelines\nRule 1", encoding="utf-8")

        result = load_system_reminder(tmp_path)

        assert result is not None
        assert "<system-reminder>" in result
        assert "# Project Guidelines" in result
        assert "Rule 1" in result
        assert "</system-reminder>" in result

    def test_file_not_exists(self, tmp_path: Path) -> None:
        """Should return None when CLAUDE.md doesn't exist."""
        result = load_system_reminder(tmp_path)
        assert result is None

    def test_empty_file(self, tmp_path: Path) -> None:
        """Should return formatted wrapper even for empty file."""
        claude_md = tmp_path / "CLAUDE.md"
        claude_md.write_text("", encoding="utf-8")

        result = load_system_reminder(tmp_path)

        assert result is not None
        assert "<system-reminder>" in result
