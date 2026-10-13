"""FastAPI application - US1: create a task."""
from fastapi import FastAPI

from app.models import Task, TaskCreate
from app.store import TaskStore

app = FastAPI(title="Task & Handover Tracker", version="0.1.0")
store = TaskStore()


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(data: TaskCreate) -> Task:
    """US1: create a task. Invalid input is rejected with 422 automatically."""
    return store.create(data)


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    """US2: list all tasks."""
    return store.list()