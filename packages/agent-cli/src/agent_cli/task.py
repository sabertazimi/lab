from typing import Literal, cast

from .singleton import Singleton

type TaskStatus = Literal["pending", "in_progress", "completed"]


class Task:
    """
    A task to be completed.
    """

    def __init__(self, content: str, status: TaskStatus, active_form: str):
        self.content = content
        self.status = status
        self.active_form = active_form


class TaskManager(metaclass=Singleton):
    """
    Manages a structured task list with enforced constraints.

    Key Design Decisions:
    --------------------
    1. Max 20 tasks: Prevents the model from creating endless lists
    2. One in_progress: Forces focus - can only work on ONE thing at a time
    3. Required fields: Each task needs content, status, and active_form

    The active_form field deserves explanation:
    - It's the PRESENT TENSE form of what's happening
    - Shown when status is "in_progress"
    - Example: content="Add tests", active_form="Adding unit tests..."

    This gives real-time visibility into what the agent is doing.
    """

    INITIAL_REMINDER = "<reminder>Use TaskUpdate for multi-step tasks.</reminder>"
    NAG_REMINDER = (
        "<reminder>10+ turns without task update. Please update tasks.</reminder>"
    )
    MAX_TASKS = 20

    def __init__(self):
        self.tasks: list[Task] = []
        self.rounds_without_task = 0
        self.completed_count = 0
        self.total_count = 0

    def update(self, tasks: list[dict[str, str]]) -> str:
        """
        Validate and update the task list.

        The model sends a complete new list each time. We validate it,
        store it, and return a rendered view that the model will see.

        Validation Rules:
        - Each task must have: content, status, active_form
        - Status must be: pending | in_progress | completed
        - Only ONE task can be in_progress at a time
        - Maximum 20 tasks allowed

        Returns:
            Rendered text view of the task list
        """
        validated_tasks: list[Task] = []
        in_progress_count = 0

        for i, task in enumerate(tasks):
            resolved_task = self.dict_to_task(task)
            content = resolved_task.content
            status = resolved_task.status
            active_form = resolved_task.active_form

            if not content:
                raise ValueError(f"Task {i}: content required")
            if status not in ["pending", "in_progress", "completed"]:
                raise ValueError(f"Task {i}: invalid status '{status}'")
            if not active_form:
                raise ValueError(f"Task {i}: active form required")

            if status == "in_progress":
                in_progress_count += 1

            validated_tasks.append(resolved_task)

        if len(validated_tasks) > TaskManager.MAX_TASKS:
            raise ValueError(f"Maximum {TaskManager.MAX_TASKS} tasks allowed")
        if in_progress_count > 1:
            raise ValueError("Only one task can be in progress at a time")

        self.tasks = validated_tasks
        return self.render()

    def render(self) -> str:
        """
        Render the task list as human-readable text.

        Format:
            ☑ Completed task
            ▣ In progress task <- Doing something...
            ☐ Pending task

            (1/3 completed)

        This rendered text is what the model sees as the tool result.
        It can then update the list based on its current state.
        """
        if not self.tasks:
            return "No tasks"

        lines: list[str] = []
        for task in self.tasks:
            if task.status == "completed":
                lines.append(f"☑ {task.content}")
            elif task.status == "in_progress":
                lines.append(f"▣ {task.content} <- {task.active_form}")
            else:
                lines.append(f"☐ {task.content}")

        self.completed_count = sum(
            1 for task in self.tasks if task.status == "completed"
        )
        self.total_count = len(self.tasks)
        lines.append(f"\n({self.completed_count}/{self.total_count} completed)")

        return "\n".join(lines)

    def increment(self) -> None:
        """
        Increment the number of rounds without a task.
        """
        self.rounds_without_task += 1

    def reset(self) -> None:
        """
        Reset the number of rounds without a task.
        """
        self.rounds_without_task = 0

    def too_long_without_task(self) -> bool:
        """
        Check if the agent has been working on tasks for too long.
        """
        return self.rounds_without_task > 10

    def dict_to_task(self, task: dict[str, str]) -> Task:
        return Task(
            content=str(task.get("content", "")).strip(),
            status=cast(TaskStatus, str(task.get("status", "pending")).strip()),
            active_form=str(task.get("active_form", "")).strip(),
        )


task_manager = TaskManager()
