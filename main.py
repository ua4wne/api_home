# https://www.youtube.com/watch?v=gBfkX9H3szQ

from typing import Optional
from typing_extensions import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager

from database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    # Clean up the ML models and release the resources

app = FastAPI(lifespan=lifespan)

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
