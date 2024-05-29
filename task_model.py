from pydantic import BaseModel


# Вынесенный класс в котором происходит валидация от BaseModel
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str


# Два создаваемых таска автоматически при старте приложения
tasks = [
    Task(id=1, title="Task 1", description="Description 1", status="in progress"),
    Task(id=2, title="Task 2", description="Description 2", status="completed")
]
