"""Unit tests for agent-cli tools module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from agent_cli.subagent import get_tools_for_agent
from agent_cli.tools import (
    BASE_TOOLS,
    execute_tool,
    run_bash,
    run_edit,
    run_glob,
    run_grep,
    run_read,
    run_skill,
    run_task_update,
    run_web_fetch,
    run_web_search,
    run_write,
    safe_path,
)


class TestSafePath:
    """Tests for safe_path() function."""

    @pytest.mark.parametrize(
        ("path", "expected_suffix"),
        [
            ("test.txt", "test.txt"),
            ("./test.txt", "test.txt"),
            ("subdir/file.txt", "subdir/file.txt"),
        ],
    )
    def test_safe_path_valid(
        self, tmp_workdir: Path, path: str, expected_suffix: str
    ) -> None:
        """Valid relative paths should resolve correctly."""
        result = safe_path(path, tmp_workdir)
        assert result == tmp_workdir / expected_suffix

    @pytest.mark.parametrize(
        "path",
        [
            "../outside.txt",
            "subdir/../../outside.txt",
            "/tmp/outside.txt",
        ],
    )
    def test_safe_path_escape_error(self, tmp_workdir: Path, path: str) -> None:
        """Paths escaping workspace should raise ValueError."""
        with pytest.raises(ValueError, match="Path escapes workspace"):
            safe_path(path, tmp_workdir)


class TestGetToolsForAgent:
    """Tests for get_tools_for_agent() function."""

    @pytest.mark.parametrize("agent_type", ["Explore", "Plan"])
    def test_get_tools_readonly_agents(self, agent_type: str) -> None:
        """Read-only agents should only have Bash and Read tools."""
        tools = get_tools_for_agent(agent_type)
        tool_names = [t["name"] for t in tools]
        assert set(tool_names) == {"Bash", "Read"}

    @pytest.mark.parametrize("agent_type", ["Code", "UnknownAgent"])
    def test_get_tools_full_access(self, agent_type: str) -> None:
        """Code agent and unknown types should have all BASE_TOOLS."""
        tools = get_tools_for_agent(agent_type)
        assert tools == BASE_TOOLS


class TestRunBash:
    """Tests for run_bash() function."""

    def test_bash_normal_command(self, tmp_workdir: Path) -> None:
        """Normal commands should return output."""
        result = run_bash("echo hello", tmp_workdir)
        assert "hello" in result

    @pytest.mark.parametrize(
        "command",
        [
            "rm -rf /",
            "sudo ls",
            "shutdown now",
            "reboot",
        ],
    )
    def test_bash_dangerous_blocked(self, tmp_workdir: Path, command: str) -> None:
        """Dangerous commands should be blocked."""
        result = run_bash(command, tmp_workdir)
        assert "Error: Dangerous command blocked" in result

    def test_bash_timeout(self, tmp_workdir: Path) -> None:
        """Command that takes too long should timeout."""
        result = run_bash("sleep 5", tmp_workdir, timeout=0.1)
        assert "Error: Command timed out" in result

    def test_bash_no_command(self, tmp_workdir: Path) -> None:
        """None command should return error."""
        result = run_bash(None, tmp_workdir)  # type: ignore[arg-type]
        assert "Error: Command is required" in result

    def test_bash_no_output(self, tmp_workdir: Path) -> None:
        """Command with no output should return (no output)."""
        result = run_bash("true", tmp_workdir)
        assert result == "(no output)"


class TestRunRead:
    """Tests for run_read() function."""

    def test_read_normal(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Normal file read should return content."""
        result = run_read("simple.txt", tmp_workdir)
        assert "line1" in result
        assert "line5" in result

    def test_read_with_limit(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Reading with limit should truncate output."""
        result = run_read("simple.txt", tmp_workdir, limit=2)
        assert "line1" in result
        assert "... (3 more lines)" in result
        assert "line5" not in result

    def test_read_nested_file(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Reading nested file should work."""
        result = run_read("subdir/nested.txt", tmp_workdir)
        assert "nested content" in result

    @pytest.mark.parametrize(
        "path",
        ["nonexistent.txt", "../outside.txt"],
    )
    def test_read_error(self, tmp_workdir: Path, path: str) -> None:
        """Invalid paths should return error."""
        result = run_read(path, tmp_workdir)
        assert "Error" in result


class TestRunWrite:
    """Tests for run_write() function."""

    def test_write_new_file(self, tmp_workdir: Path) -> None:
        """Writing new file should create it with correct content."""
        result = run_write("new_file.txt", "Hello, World!", tmp_workdir)
        assert "Wrote" in result
        assert "13 bytes" in result

        file_path = tmp_workdir / "new_file.txt"
        assert file_path.exists()
        assert file_path.read_text(encoding="utf-8") == "Hello, World!"

    def test_write_create_dirs(self, tmp_workdir: Path) -> None:
        """Writing should create parent directories if needed."""
        result = run_write("deep/nested/dir/file.txt", "content", tmp_workdir)
        assert "Wrote" in result
        assert (tmp_workdir / "deep" / "nested" / "dir" / "file.txt").exists()

    def test_write_overwrite(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Writing existing file should overwrite it."""
        run_write("simple.txt", "new content", tmp_workdir)
        assert sample_files["simple.txt"].read_text(encoding="utf-8") == "new content"

    def test_write_outside_workdir(self, tmp_workdir: Path) -> None:
        """Writing outside workspace should return error."""
        result = run_write("../outside.txt", "content", tmp_workdir)
        assert "Error" in result


class TestRunEdit:
    """Tests for run_edit() function."""

    def test_edit_replace(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Editing should replace text correctly."""
        result = run_edit("simple.txt", "line2", "modified_line2", tmp_workdir)
        assert "Edited" in result

        content = sample_files["simple.txt"].read_text(encoding="utf-8")
        assert "modified_line2" in content
        assert "line1" in content

    def test_edit_not_found(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Editing with nonexistent text should return error."""
        result = run_edit("simple.txt", "nonexistent_text", "replacement", tmp_workdir)
        assert "Error: Text not found" in result

    def test_edit_first_occurrence(self, tmp_workdir: Path) -> None:
        """Editing should only replace first occurrence."""
        test_file = tmp_workdir / "repeated.txt"
        test_file.write_text("hello hello hello", encoding="utf-8")

        run_edit("repeated.txt", "hello", "goodbye", tmp_workdir)
        assert test_file.read_text(encoding="utf-8") == "goodbye hello hello"

    @pytest.mark.parametrize(
        "path",
        ["nonexistent.txt", "../outside.txt"],
    )
    def test_edit_error(self, tmp_workdir: Path, path: str) -> None:
        """Invalid paths should return error."""
        result = run_edit(path, "old", "new", tmp_workdir)
        assert "Error" in result


class TestRunGlob:
    """Tests for run_glob() function."""

    @pytest.mark.parametrize(
        ("pattern", "expected"),
        [
            ("*.txt", "simple.txt"),
            ("*.py", "sample.py"),
        ],
    )
    def test_glob_match(
        self,
        tmp_workdir: Path,
        sample_files: dict[str, Path],
        pattern: str,
        expected: str,
    ) -> None:
        """Glob should match files with pattern."""
        result = run_glob(pattern, tmp_workdir)
        assert expected in result

    def test_glob_recursive(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Glob with ** should match recursively."""
        result = run_glob("**/*.py", tmp_workdir)
        assert "sample.py" in result
        assert "module.py" in result

    def test_glob_no_match(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Glob with no matches should return (no matches)."""
        result = run_glob("*.nonexistent", tmp_workdir)
        assert result == "(no matches)"

    def test_glob_with_path(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Glob with specific path should search only that directory."""
        result = run_glob("*.py", tmp_workdir, "subdir")
        assert "module.py" in result
        assert "sample.py" not in result

    def test_glob_outside_workdir(self, tmp_workdir: Path) -> None:
        """Glob outside workspace should return error."""
        result = run_glob("*", tmp_workdir, "../")
        assert "Error" in result


class TestRunGrep:
    """Tests for run_grep() function."""

    def test_grep_content_mode(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep in content mode should return matching lines with line numbers."""
        result = run_grep("def hello", tmp_workdir)
        assert "sample.py" in result
        assert "def hello" in result

    def test_grep_files_mode(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep in files_with_matches mode should return only file names."""
        result = run_grep("def", tmp_workdir, output_mode="files_with_matches")
        assert "sample.py" in result
        assert "def hello" not in result

    def test_grep_count_mode(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep in count mode should return match counts."""
        result = run_grep("def", tmp_workdir, output_mode="count")
        assert "sample.py" in result

    def test_grep_case_insensitive(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep with i=True should be case insensitive."""
        result = run_grep("HELLO", tmp_workdir, i=True)
        assert "sample.py" in result

    def test_grep_with_glob_filter(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep with glob filter should only search matching files."""
        result = run_grep("content", tmp_workdir, glob="*.txt")
        assert "nested.txt" in result
        assert "sample.py" not in result

    def test_grep_head_limit(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep with head_limit should limit results."""
        result = run_grep("def", tmp_workdir, head_limit=1)
        assert len(result.strip().split("\n")) == 1

    def test_grep_invalid_regex(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep with invalid regex should return error."""
        result = run_grep("[invalid", tmp_workdir)
        assert "Error: Invalid regex pattern" in result

    def test_grep_no_matches(
        self, tmp_workdir: Path, sample_files: dict[str, Path]
    ) -> None:
        """Grep with no matches should return (no matches)."""
        result = run_grep("xyz123nonexistent", tmp_workdir)
        assert result == "(no matches)"


class TestWebSearch:
    """Tests for run_web_search() function."""

    def test_web_search_success(self) -> None:
        """Web search should return formatted results."""
        mock_results = [
            {
                "title": "Test Title",
                "href": "https://example.com/page",
                "body": "Test body content",
            },
        ]

        with patch("ddgs.DDGS") as mock_ddgs_class:
            mock_ddgs = MagicMock()
            mock_ddgs.text.return_value = mock_results
            mock_ddgs_class.return_value = mock_ddgs

            result = run_web_search("test query")

            assert "Test Title" in result
            assert "https://example.com/page" in result

    def test_web_search_no_results(self) -> None:
        """Web search with no results should return (no results)."""
        with patch("ddgs.DDGS") as mock_ddgs_class:
            mock_ddgs = MagicMock()
            mock_ddgs.text.return_value = []
            mock_ddgs_class.return_value = mock_ddgs

            assert run_web_search("test") == "(no results)"

    def test_web_search_domain_filters(self) -> None:
        """Web search should filter by allowed/blocked domains."""
        mock_results = [
            {"title": "GitHub", "href": "https://github.com/page", "body": "GitHub"},
            {"title": "Other", "href": "https://other.com/page", "body": "Other"},
        ]

        with patch("ddgs.DDGS") as mock_ddgs_class:
            mock_ddgs = MagicMock()
            mock_ddgs.text.return_value = mock_results
            mock_ddgs_class.return_value = mock_ddgs

            result = run_web_search("test", allowed_domains=["github.com"])

            assert "GitHub" in result
            assert "Other" not in result

    def test_web_search_exception(self) -> None:
        """Web search exception should return error message."""
        with patch("ddgs.DDGS") as mock_ddgs_class:
            mock_ddgs_class.side_effect = Exception("Network error")
            assert "Search failed" in run_web_search("test")


class TestWebFetch:
    """Tests for run_web_fetch() function."""

    def test_web_fetch_success(self) -> None:
        """Web fetch should return markdown content."""
        mock_response = MagicMock()
        mock_response.text = "<html><body><h1>Title</h1><p>Content</p></body></html>"
        mock_response.raise_for_status = MagicMock()

        from agent_cli.tools import fetch_cached

        fetch_cached.cache_clear()

        with patch("httpx.get", return_value=mock_response):
            result = run_web_fetch("https://example.com", "Get content")
            assert "Title" in result or "Content" in result

    def test_web_fetch_http_upgrade(self) -> None:
        """Web fetch should upgrade HTTP to HTTPS."""
        mock_response = MagicMock()
        mock_response.text = "<html><body>Content</body></html>"
        mock_response.raise_for_status = MagicMock()

        from agent_cli.tools import fetch_cached

        fetch_cached.cache_clear()

        with patch("httpx.get", return_value=mock_response) as mock_get:
            run_web_fetch("http://example.com", "Get content")
            assert mock_get.call_args[0][0].startswith("https://")

    def test_web_fetch_exception(self) -> None:
        """Web fetch exception should return error message."""
        from agent_cli.tools import fetch_cached

        fetch_cached.cache_clear()

        with patch("httpx.get", side_effect=Exception("Connection error")):
            assert "Fetch failed" in run_web_fetch("https://example.com", "Get content")


class TestTaskUpdate:
    """Tests for run_task_update() function."""

    def test_task_update_valid(self, mock_task_manager: MagicMock) -> None:
        """Valid task update should succeed."""
        tasks = [
            {"content": "Task 1", "status": "pending", "active_form": "Working on 1"},
        ]

        result = run_task_update(tasks, mock_task_manager)

        mock_task_manager.update.assert_called_once_with(tasks)
        assert result == "Tasks updated"

    def test_task_update_error(self, mock_task_manager: MagicMock) -> None:
        """Task update error should return error message."""
        mock_task_manager.update.side_effect = ValueError("Invalid status")
        result = run_task_update(
            [{"content": "Task", "status": "invalid", "active_form": "X"}],
            mock_task_manager,
        )
        assert "Error" in result


class TestRunSkill:
    """Tests for run_skill() function."""

    def test_skill_found(self, mock_skill_loader: MagicMock) -> None:
        """Found skill should return wrapped content."""
        mock_skill_loader.get_skill.return_value = "# Skill Content\nInstructions"

        result = run_skill("test-skill", mock_skill_loader)

        mock_skill_loader.get_skill.assert_called_once_with("test-skill")
        assert '<skill-loaded name="test-skill">' in result
        assert "# Skill Content" in result

    @pytest.mark.parametrize(
        ("available_skills", "expected_list"),
        [
            (["skill1", "skill2"], "skill1, skill2"),
            ([], "none"),
        ],
    )
    def test_skill_not_found(
        self,
        mock_skill_loader: MagicMock,
        available_skills: list[str],
        expected_list: str,
    ) -> None:
        """Not found skill should return error with available skills."""
        mock_skill_loader.get_skill.return_value = None
        mock_skill_loader.list_skills.return_value = available_skills

        result = run_skill("nonexistent", mock_skill_loader)

        assert "Error: Unknown skill" in result
        assert expected_list in result


class TestExecuteTool:
    """Tests for execute_tool() function - verifies tool dispatch."""

    def test_execute_unknown_tool(
        self, tmp_workdir: Path, mock_skill_loader: MagicMock
    ) -> None:
        """Execute unknown tool should return error."""
        mock_ui = MagicMock()
        result = execute_tool(
            mock_ui,
            "UnknownTool",
            {},
            workdir=tmp_workdir,
            skill_loader=mock_skill_loader,
        )
        assert "Unknown tool: UnknownTool" in result
