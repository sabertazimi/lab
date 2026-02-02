"""Unit tests for agent-cli output module."""

from unittest.mock import MagicMock

import pytest
from agent_cli.output import get_tool_call_detail, get_tool_result_preview
from agent_cli.ui_textual import TextualOutput
from rich.text import Text


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
            (
                "WebReader",
                {"url": "https://example.com"},
                "WebReader(https://example.com)",
            ),
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


class TestTextualOutputThinking:
    """Tests for TextualOutput.thinking() method."""

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Set up output instance for each test."""
        # Create mocks for callbacks
        self.mock_chat_log = MagicMock()
        self.mock_status_bar = MagicMock()
        self.mock_thinking_log = MagicMock()
        self.thinking_history: list[Text] = []
        self.show_thinking = False

        # Create TextualOutput with callback functions
        self.output = TextualOutput(
            get_chat_log=lambda: self.mock_chat_log,
            get_status_bar=lambda: self.mock_status_bar,
            get_thinking_log=lambda: self.mock_thinking_log,
            store_thinking=lambda t: self.thinking_history.append(t),
            is_thinking_view=lambda: self.show_thinking,
        )

    def test_thinking_none_content(self) -> None:
        """None content should return early without side effects."""
        self.output.thinking(None)
        assert len(self.thinking_history) == 0

    def test_thinking_single_line(self) -> None:
        """Single-line content should be formatted and stored."""
        content = "Single line thinking"
        self.output.thinking(content)
        assert len(self.thinking_history) == 1
        history_entry = self.thinking_history[0]
        assert isinstance(history_entry, Text)
        assert "Single line thinking" in history_entry.plain

    def test_thinking_multiline(self) -> None:
        """Multi-line content should have proper indentation."""
        content = "First line\nSecond line\nThird line"
        self.output.thinking(content)
        assert len(self.thinking_history) == 1
        history_entry = self.thinking_history[0]
        plain = history_entry.plain
        assert "First line" in plain
        assert "Second line" in plain
        assert "Third line" in plain

    def test_thinking_with_duration(self) -> None:
        """Duration should be formatted in chat indicator."""
        content = "Thinking with duration"
        duration = 1.5
        self.output.thinking(content, duration=duration)
        assert len(self.thinking_history) == 1
        # Check that the chat log was written with duration info
        assert self.mock_chat_log.write.called
        written_text = str(self.mock_chat_log.write.call_args)
        assert "1.5s" in written_text or "1.5" in written_text

    def test_thinking_history_updated(self) -> None:
        """thinking_history should contain formatted content."""
        content = "Test thinking content"
        self.output.thinking(content)
        assert len(self.thinking_history) == 1
        history_entry = self.thinking_history[0]
        assert isinstance(history_entry, Text)
        # Should have blue bullet indicator
        assert "Test thinking content" in history_entry.plain

    def test_thinking_updates_log_when_visible(self) -> None:
        """When show_thinking=True, log should be updated."""
        self.show_thinking = True
        content = "Thinking when visible"
        self.output.thinking(content)
        # Check that thinking log was written to
        assert self.mock_thinking_log.write.called

    def test_thinking_multiple_calls(self) -> None:
        """Multiple calls should append to history."""
        self.output.thinking("First thought")
        self.output.thinking("Second thought")
        self.output.thinking("Third thought")
        assert len(self.thinking_history) == 3

    def test_format_thinking_block_empty(self) -> None:
        """Empty content should handle gracefully."""
        # pyright: ignore[reportPrivateUsage]
        result = self.output._format_thinking_block("")  # pyright: ignore[reportPrivateUsage]
        assert isinstance(result, Text)

    def test_format_thinking_block_single_line(self) -> None:
        """Single line should have blue bullet."""
        content = "Single line"
        # pyright: ignore[reportPrivateUsage]
        result = self.output._format_thinking_block(content)  # pyright: ignore[reportPrivateUsage]
        assert isinstance(result, Text)
        plain = result.plain
        assert "Single line" in plain

    def test_format_thinking_block_multiline(self) -> None:
        """Multi-line should have proper indentation."""
        content = "Line 1\nLine 2\nLine 3"
        # pyright: ignore[reportPrivateUsage]
        result = self.output._format_thinking_block(content)  # pyright: ignore[reportPrivateUsage]
        assert isinstance(result, Text)
        plain = result.plain
        assert "Line 1" in plain
        assert "Line 2" in plain
        assert "Line 3" in plain
