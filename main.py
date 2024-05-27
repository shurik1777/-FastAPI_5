"""
Задание №1
Создать, API для управления списком задач. Приложение должно иметь
возможность создавать, обновлять, удалять и получать список задач.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Task с полями id, title, description и status.
Создайте список tasks для хранения задач.
Создайте маршрут для получения списка задач (метод GET).
Создайте маршрут для создания новой задачи (метод POST).
Создайте маршрут для обновления задачи (метод PUT).
Создайте маршрут для удаления задачи (метод DELETE).
Реализуйте валидацию данных запроса и ответа
"""
from fastapi import FastAPI, HTTPException
from typing import List
import logging
from task_model import Task, tasks

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks


@app.post("/create_task")
async def create_task(task: Task):
    tasks.append(task)
    return {"message": "Task created successfully"}


# @app.put("/tasks/{task_id}", response_model=Task)
# async def update_task(task_id: int, task: Task):
#     for num in range(len(tasks)):
#         if tasks[num].id == task_id:
#             tasks[num] = task
#             print(f"{tasks[num]} изменен")
#             return tasks[num]
#     raise HTTPException(status_code=404, detail='Task not found')


@app.put("/update_task/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = updated_task
            logger.info(f'Task id={task.id} {task.title} - успешно добавлен')
            return {"message": "Task updated successfully"}

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/delete_task/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[i]
            logger.info(f'Task id={task.id} {task.title} - успешно добавлен')
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fastapi_app:app", host="127.0.0.1", port=8000, reload=True)
