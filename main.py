from typing import Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan():
    await delete_tables()
    await create_tables()
    yield



app = FastAPI()


class SchemaTaskAdd(BaseModel):
    name: str
    description: str | None = None


class SchemaTask(SchemaTaskAdd):
    id: int


tasks = []


@app.post("/tasks")
async def add_task(task: Annotated[SchemaTaskAdd, Depends()]):
    tasks.append(task)
    return {"ok": True}
