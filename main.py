# https://www.youtube.com/watch?v=gBfkX9H3szQ

from typing import Optional
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int


tasks = []
@app.post("/tasks")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}


# @app.get(("/task"))
# def get_tasks():
#     task = Task(name="My first task")
#     return {"data": task}
