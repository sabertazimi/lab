"""Unit tests for agent-cli output module."""

import pytest
from agent_cli.output import get_tool_call_detail, get_tool_result_preview


class TestGetToolCallDetail:
    """Tests for get_tool_call_detail() function."""

    @pytest.mark.parametrize(
        ("name", "tool_input", "expected"),
        [
            ("Bash", {"command": "echo hello"}, "Bash(echo hello)"),
            ("Read", {"path": "file.txt"}, "Read(file.txt)"),
            ("Write", {"path": "new.txt", "content": "x"}, "Write(new.txt)"),
            ("Edit", {"path": "edit.txt"}, "Edit(edit.txt)"),
            ("Glob", {"pattern": "*.py"}, "Glob(*.py)"),
            ("Grep", {"pattern": "def"}, "Grep(def)"),
            ("WebSearch", {"query": "python docs"}, "WebSearch(python docs)"),
            ("WebReader", {"url": "https://example.com"}, "WebReader(https://example.com)"),
            ("TaskUpdate", {"list_title": "My Tasks"}, "TaskUpdate(My Tasks)"),
            ("Task", {"description": "Explore code"}, "Task(Explore code)"),
            ("Skill", {"skill_name": "test-skill"}, "Skill(test-skill)"),
        ],
    )
    def test_known_tools(
        self, name: str, tool_input: dict[str, object], expected: str
    ) -> None:
        """Known tools should format with their key argument."""
        assert get_tool_call_detail(name, tool_input) == expected

    def test_unknown_tool(self) -> None:
        """Unknown tools should format with full input dict."""
        result = get_tool_call_detail("CustomTool", {"foo": "bar"})
        assert "CustomTool(" in result
        assert "foo" in result


class TestGetToolResultPreview:
    """Tests for get_tool_result_preview() function."""

    def test_none_output(self) -> None:
        """None output should return 'Empty'."""
        assert get_tool_result_preview(None) == "Empty"

    def test_short_output(self) -> None:
        """Short output should be returned with prefix."""
        result = get_tool_result_preview("Hello")
        assert "⎿" in result
        assert "Hello" in result

    def test_truncation(self) -> None:
        """Long output should be truncated with ellipsis."""
        long_text = "x" * 300
        result = get_tool_result_preview(long_text, max_length=200)
        assert "..." in result
        assert len(result) < 300

    def test_multiline_indent(self) -> None:
        """Multiline output should have aligned indentation."""
        result = get_tool_result_preview("line1\nline2\nline3")
        # Second line should be indented
        assert "\n     " in result

    def test_whitespace_stripped(self) -> None:
        """Leading/trailing whitespace should be stripped."""
        result = get_tool_result_preview("  content  \n  ")
        assert result.endswith("content")
