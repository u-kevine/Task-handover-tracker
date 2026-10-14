from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Priority = Literal["low", "medium", "high"]


class TaskCreate(BaseModel):
    """What the client sends when creating a task (US1, US4)."""

    # Strip spaces first, so "   " becomes "" and fails min_length.
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    priority: Priority = "medium"


class Task(BaseModel):
    """A stored task, as returned by the API."""

    id: int
    title: str
    description: str
    priority: Priority = "medium"
    completed: bool = False
    created_at: datetime
