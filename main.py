import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# Необходимо создать API для управления списком задач. 
# Каждая задача должна содержать заголовок и описание. 
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

# API должен содержать следующие конечные точки:
# — GET /tasks — возвращает список всех задач.
# — GET /tasks/{id} — возвращает задачу с указанным идентификатором.
# — POST /tasks — добавляет новую задачу.
# — PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
# — DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа. 
# Для этого использовать библиотеку Pydantic.


app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

list_of_tasks = []

def get_task(id):
    return [task for task in list_of_tasks if task.id == id][0]

@app.get("/tasks")
async def get_all_tasks():
    """возвращает список всех задач."""
    return list_of_tasks

@app.get("/tasks/{id}")
async def get_task_by_id(task_id: int):
    """возвращает задачу с указанным идентификатором.
    """    
    return get_task(task_id)


@app.post("/tasks")
async def add_task(task: Task):
    """добавляет новую задачу.
    """
    list_of_tasks.append(task)
    return task

@app.put("/tasks/{id}")
async def update_task(task_id: int, task_update: Task):
    """обновляет задачу с указанным идентификатором.
    """
    tast_exiting = get_task(task_id)
    
    if tast_exiting and task_id == task_update.id:
        list_of_tasks[list_of_tasks.index(tast_exiting)] = task_update
        return task_update
    else:
        return None
    
@app.delete("/tasks/{id}")
async def delete_task(task_id: int):
    """удаляет задачу с указанным идентификатором.
    """
    tast_exiting = get_task(task_id)    
    if tast_exiting:
        list_of_tasks.remove(tast_exiting)
        return tast_exiting
    else:
        return None
    


def generate_tasks():    
    for i in range(6):
        list_of_tasks.append(Task(id = i, 
                                  title=f'Task_{i}', 
                                  description='task description', 
                                  is_completed=False))
    print(*list_of_tasks, sep='\n')



generate_tasks()
if __name__ == "__main__":        
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("this")