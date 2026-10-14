"""FastAPI application for the Task & Handover Tracker."""
import logging
import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.models import Priority, Task, TaskCreate
from app.store import TaskStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("tracker")

app = FastAPI(title="Task & Handover Tracker", version="0.2.0")
store = TaskStore()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    """US8: log method, path, status code and duration for every request."""
    start = time.perf_counter()
    try:
        response = await call_next(request)
    except Exception:
        # US8: log the stack trace and hide details from the client.
        logger.exception("Unhandled error on %s %s", request.method, request.url.path)
        response = JSONResponse(status_code=500, content={"detail": "Internal server error"})
    duration_ms = (time.perf_counter() - start) * 1000
    logger.info(
        "%s %s -> %s (%.1f ms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


@app.get("/health")
def health() -> dict:
    """US7: health check for monitoring."""
    return {"status": "ok", "version": app.version, "task_count": len(store.list())}


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(data: TaskCreate) -> Task:
    """US1/US4: create a task. Invalid input is rejected with 422 automatically."""
    task = store.create(data)
    logger.info("Created task %s", task.id)
    return task


@app.get("/tasks", response_model=list[Task])
def list_tasks(completed: bool | None = None, priority: Priority | None = None) -> list[Task]:
    """US2/US5: list tasks, optionally filtered by status and/or priority."""
    return store.list(completed=completed, priority=priority)


@app.patch("/tasks/{task_id}/complete", response_model=Task)
def complete_task(task_id: int) -> Task:
    """US3: mark a task as complete."""
    task = store.complete(task_id)
    if task is None:
        logger.warning("Task %s not found", task_id)
        raise HTTPException(status_code=404, detail="Task not found")
    return task
