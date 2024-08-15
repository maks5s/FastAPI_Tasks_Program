from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository
from schemas import SchemaTaskAdd, SchemaTask, SchemaTaskId

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("")
async def add_task(task: Annotated[SchemaTaskAdd, Depends()]) -> SchemaTaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

# dfh
@router.get("")
async def get_tasks() -> list[SchemaTask]:
    tasks = await TaskRepository.find_all()
    return tasks
