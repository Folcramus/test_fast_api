from typing import Annotated

from fastapi import APIRouter, Depends
from repository import TaskRepository

from schema import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/task",
    tags=["таски"]

)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:

    task_id = await TaskRepository.add_one(task)

    return {"ok": True, "task_id": task_id}



@router.get("")
async def view_task() -> list[STask]:
    tasks = await TaskRepository.find_all()

    return tasks
