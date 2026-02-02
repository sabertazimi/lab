"""Unit tests for agent-cli task module."""

import pytest
from agent_cli.task import Task, TaskManager


class TestTask:
    """Tests for Task class."""

    def test_task_init(self) -> None:
        """Task should store content, status, and active_form."""
        task = Task("Do something", "pending", "Doing something")
        assert task.content == "Do something"
        assert task.status == "pending"
        assert task.active_form == "Doing something"


class TestTaskManager:
    """Tests for TaskManager class."""

    def test_update_valid_tasks(self) -> None:
        """Valid tasks should be stored and rendered."""
        manager = TaskManager()
        tasks = [
            {"content": "Task 1", "status": "pending", "active_form": "Working on 1"},
            {"content": "Task 2", "status": "completed", "active_form": "Done 2"},
        ]

        result = manager.update(tasks)

        assert len(manager.tasks) == 2
        assert "Task 1" in result
        assert "Task 2" in result

    def test_update_missing_content(self) -> None:
        """Task without content should raise ValueError."""
        manager = TaskManager()
        with pytest.raises(ValueError, match="content required"):
            manager.update([{"status": "pending", "active_form": "X"}])

    def test_update_missing_active_form(self) -> None:
        """Task without active_form should raise ValueError."""
        manager = TaskManager()
        with pytest.raises(ValueError, match="active form required"):
            manager.update([{"content": "Task", "status": "pending"}])

    def test_update_invalid_status(self) -> None:
        """Task with invalid status should raise ValueError."""
        manager = TaskManager()
        with pytest.raises(ValueError, match="invalid status"):
            manager.update(
                [{"content": "Task", "status": "invalid", "active_form": "X"}]
            )

    def test_update_multiple_in_progress(self) -> None:
        """Multiple in_progress tasks should raise ValueError."""
        manager = TaskManager()
        tasks = [
            {"content": "Task 1", "status": "in_progress", "active_form": "X"},
            {"content": "Task 2", "status": "in_progress", "active_form": "Y"},
        ]
        with pytest.raises(ValueError, match="Only one task can be in progress"):
            manager.update(tasks)

    def test_update_exceeds_max_tasks(self) -> None:
        """Exceeding MAX_TASKS should raise ValueError."""
        manager = TaskManager()
        tasks = [
            {"content": f"Task {i}", "status": "pending", "active_form": f"X{i}"}
            for i in range(TaskManager.MAX_TASKS + 1)
        ]
        with pytest.raises(ValueError, match=f"Maximum {TaskManager.MAX_TASKS} tasks"):
            manager.update(tasks)

    def test_render_empty(self) -> None:
        """Empty task list should render 'No tasks'."""
        manager = TaskManager()
        assert manager.render() == "No tasks"

    def test_render_all_statuses(self) -> None:
        """Render should show correct icons for each status."""
        manager = TaskManager()
        manager.update(
            [
                {"content": "Done", "status": "completed", "active_form": "X"},
                {"content": "Working", "status": "in_progress", "active_form": "Busy"},
                {"content": "Todo", "status": "pending", "active_form": "X"},
            ]
        )

        result = manager.render()
        assert "✔ Done" in result
        assert "▣ Working <- Busy" in result
        assert "☐ Todo" in result
        assert "(1/3 completed)" in result

    def test_increment_and_reset(self) -> None:
        """increment() and reset() should manage rounds_without_task."""
        manager = TaskManager()
        assert manager.rounds_without_task == 0

        manager.increment()
        manager.increment()
        assert manager.rounds_without_task == 2

        manager.reset()
        assert manager.rounds_without_task == 0

    def test_too_long_without_task(self) -> None:
        """too_long_without_task() should return True after 10 rounds."""
        manager = TaskManager()
        assert not manager.too_long_without_task()

        for _ in range(11):
            manager.increment()

        assert manager.too_long_without_task()

    def test_dict_to_task_strips_whitespace(self) -> None:
        """_dict_to_task should strip whitespace from values."""
        manager = TaskManager()
        # pyright: ignore[reportPrivateUsage]
        task = manager._dict_to_task(  # pyright: ignore[reportPrivateUsage]
            {"content": "  Task  ", "status": "  pending  ", "active_form": "  X  "}
        )
        assert task.content == "Task"
        assert task.status == "pending"
        assert task.active_form == "X"
