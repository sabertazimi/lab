"""Shared fixtures for agent-cli tests."""

from pathlib import Path
from unittest.mock import MagicMock

import pytest


@pytest.fixture
def tmp_workdir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """
    Create a temporary working directory and patch WORKDIR.

    This fixture:
    1. Creates an isolated temp directory for each test
    2. Patches llm.WORKDIR to point to the temp directory
    3. Patches tools.WORKDIR (imported from llm) as well

    Returns the temp path for test assertions.
    """
    # Patch the WORKDIR in llm module (source of truth)
    from agent_cli import llm

    monkeypatch.setattr(llm, "WORKDIR", tmp_path)

    # Also need to patch it in tools module since it imports at module level
    from agent_cli import tools

    monkeypatch.setattr(tools, "WORKDIR", tmp_path)

    return tmp_path


@pytest.fixture
def mock_task_manager(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """
    Mock the task_manager singleton.

    Returns a MagicMock that can be configured for specific test scenarios.
    """
    from agent_cli import task as task_module
    from agent_cli import tools

    mock = MagicMock()
    mock.update.return_value = "Tasks updated"

    monkeypatch.setattr(task_module, "task_manager", mock)
    monkeypatch.setattr(tools, "task_manager", mock)

    return mock


@pytest.fixture
def mock_skill_loader(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """
    Mock the skill_loader singleton.

    Returns a MagicMock that can be configured for specific test scenarios.
    """
    from agent_cli import skill as skill_module
    from agent_cli import tools

    mock = MagicMock()
    mock.get_skill.return_value = None
    mock.list_skills.return_value = []

    monkeypatch.setattr(skill_module, "skill_loader", mock)
    monkeypatch.setattr(tools, "skill_loader", mock)

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
