from typing import List
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


tasks = [
    Task(id=1, title="Task 1", description="Description 1", status="in progress"),
    Task(id=2, title="Task 2", description="Description 2", status="completed")
]
