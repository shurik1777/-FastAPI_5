from pydantic import BaseModel


# Вынесенный класс в котором происходит валидация от BaseModel
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
