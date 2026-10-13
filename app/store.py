"""A simple in-memory store."""
from datetime import datetime, timezone

from app.models import Task, TaskCreate


class TaskStore:
    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def create(self, data: TaskCreate) -> Task:
        task = Task(
            id=self._next_id,
            title=data.title,
            description=data.description,
            created_at=datetime.now(timezone.utc),
        )
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def list(self) -> list[Task]:
        return list(self._tasks.values())

    def clear(self) -> None:
        """Used by tests to reset state between runs."""
        self._tasks.clear()
        self._next_id = 1