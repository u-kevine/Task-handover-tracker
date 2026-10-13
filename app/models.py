"""Data models (schemas) for the Task & Handover Tracker."""
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """What the client sends when creating a task (US1)."""

    # Strip spaces first, so "   " becomes "" and fails min_length.
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


class Task(BaseModel):
    """A stored task, as returned by the API."""

    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime
