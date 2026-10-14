from datetime import datetime, timezone

from app.models import Priority, Task, TaskCreate


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def create(self, data: TaskCreate) -> Task:
        task = Task(
            id=self._next_id,
            title=data.title,
            description=data.description,
            priority=data.priority,
            created_at=datetime.now(timezone.utc),
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list(
        self, completed: bool | None = None, priority: Priority | None = None
    ) -> list[Task]:
        tasks = list(self._tasks.values())
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]
        if priority is not None:
            tasks = [t for t in tasks if t.priority == priority]
        return tasks

    def complete(self, task_id: int) -> Task | None:
        task = self._tasks.get(task_id)
        if task is not None:
            task.completed = True
        return task

    def clear(self) -> None:
        """Used by tests to reset state between runs."""
        self._tasks.clear()
        self._next_id = 1
