"""
Необходимо создать API для управления списком задач.
Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List
import logging
from task_model import Task

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tasks = []


# GET /tasks — возвращает список всех задач (т. е. задекорировал маршрут
# /tasks запросом .get, передав через модель весь список задач)
@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


# GET /tasks/{id} - возвращает конкретную задачу по ее id, если она не найдена
# выдает ошибку, что Задача не найдена
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    logger.info('Отработал GET_ID запрос.')
    for i in tasks:
        if i.id == task_id:
            return i
    raise HTTPException(status_code=404, detail="Задача не найдена")


# POST /tasks/ — добавляет новую задачу с проверкой по id
@app.post('/tasks', response_model=Task)
async def create_task(task: Task):
    logger.info('Отработал POST запрос.')
    # Проверка на уникальность ID
    for i in tasks:
        if i.id == task.id:
            raise HTTPException(status_code=400, detail="Задача с таким идентификатором уже существует")
    tasks.append(task)
    return task


# PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            logger.info(f'Task id={task.id} {task.title} - успешно обновлен')
            return {"message": "Task updated successfully"}

    raise HTTPException(status_code=404, detail="Task not found")


# DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.
@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            logger.info(f'Task id={task.id} {task.title} - успешно удален')
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)
