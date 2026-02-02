"""Shared fixtures for agent-cli tests."""

from pathlib import Path
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tmp_workdir(tmp_path: Path) -> Path:
    """
    Create a temporary working directory for testing.

    Returns the temp path for test assertions.
    """
    return tmp_path


@pytest.fixture
def mock_task_manager() -> MagicMock:
    """
    Create a mock TaskManager.

    Returns a MagicMock that can be configured for specific test scenarios.
    """
    mock = MagicMock()
    mock.update.return_value = "Tasks updated"
    mock.INITIAL_REMINDER = "<reminder>Use TaskUpdate for multi-step tasks.</reminder>"
    mock.NAG_REMINDER = (
        "<reminder>10+ turns without task update. Please update tasks.</reminder>"
    )
    mock.too_long_without_task.return_value = False
    return mock


@pytest.fixture
def mock_skill_loader(tmp_workdir: Path) -> MagicMock:
    """
    Create a mock SkillLoader.

    Returns a MagicMock that can be configured for specific test scenarios.
    """
    mock = MagicMock()
    mock.get_skill.return_value = None
    mock.list_skills.return_value = []
    mock.get_descriptions.return_value = "(no skills available)"
    mock.skills = {}
    return mock


@pytest.fixture
def clear_singleton():
    """
    Clear Singleton instances before and after test.

    This fixture ensures each test gets a fresh singleton instance.
    Yields control to test, then cleans up after.
    """
    from agent_cli.singleton import Singleton

    # Clear before test (accessing protected member is intentional for testing)
    Singleton._instances.clear()  # pyright: ignore[reportPrivateUsage]
    yield
    # Clear after test
    Singleton._instances.clear()  # pyright: ignore[reportPrivateUsage]


@pytest.fixture
def sample_files(tmp_workdir: Path) -> dict[str, Path]:
    """
    Create sample files for testing file operations.

    Returns a dict mapping file names to their paths.
    """
    files: dict[str, Path] = {}

    # Simple text file
    simple_txt = tmp_workdir / "simple.txt"
    simple_txt.write_text("line1\nline2\nline3\nline4\nline5\n", encoding="utf-8")
    files["simple.txt"] = simple_txt

    # Python file for grep tests
    sample_py = tmp_workdir / "sample.py"
    sample_py.write_text(
        """def hello():
    print("Hello, World!")

def goodbye():
    print("Goodbye!")

class MyClass:
    def method(self):
        pass
""",
        encoding="utf-8",
    )
    files["sample.py"] = sample_py

    # Nested directory structure
    subdir = tmp_workdir / "subdir"
    subdir.mkdir()

    nested_txt = subdir / "nested.txt"
    nested_txt.write_text("nested content\n", encoding="utf-8")
    files["subdir/nested.txt"] = nested_txt

    nested_py = subdir / "module.py"
    nested_py.write_text("# Python module\ndef func():\n    pass\n", encoding="utf-8")
    files["subdir/module.py"] = nested_py

    return files


@pytest.fixture
def mock_ui() -> MagicMock:
    """
    Create a mock IAgentUI implementation.

    Returns a MagicMock that implements the IAgentUI protocol.
    """
    mock = MagicMock()
    mock.text = MagicMock()
    mock.newline = MagicMock()
    mock.clear = MagicMock()
    mock.primary = MagicMock()
    mock.accent = MagicMock()
    mock.error = MagicMock()
    mock.debug = MagicMock()
    mock.thinking = MagicMock()
    mock.response = MagicMock()
    mock.tool_call = MagicMock()
    mock.tool_result = MagicMock()
    mock.interrupted = MagicMock()
    mock.status = MagicMock()
    mock.banner = MagicMock()
    return mock
