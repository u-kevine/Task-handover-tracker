from fastapi import FastAPI, HTTPException

from app.models import Priority, Task, TaskCreate
from app.store import TaskStore

app = FastAPI(title="Task & Handover Tracker", version="0.1.0")
store = TaskStore()


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(data: TaskCreate) -> Task:
    """US1/US4: create a task. Invalid input is rejected with 422 automatically."""
    return store.create(data)


@app.get("/tasks", response_model=list[Task])
def list_tasks(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    """US2/US5: list tasks, optionally filtered by status and/or priority."""
    return store.list(completed=completed, priority=priority)


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int) -> Task:
    """US3: mark a task as complete."""
    task = store.complete(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
