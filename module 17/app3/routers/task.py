from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel


router = APIRouter(
    prefix="/task",
    tags=["task"]
)


class TaskResponse(BaseModel):
    id: int
    priority: int
    user_id: int
    content: str
    title: str
    completed: bool
    slug: str



@router.get("/", response_model=list[TaskResponse])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    query = select(Task)
    result = db.scalars(query).all()
    return result


@router.get("/task_id")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    result = db.scalars(query).first()

    if result is not None:
        return result
    else:
        raise HTTPException(status_code=404, detail="Task was not found")


@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка существования пользователя
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = insert(Task).values(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id,
        slug=slugify(task.title)
    )

    try:
        db.execute(new_task)
        db.commit()

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Integrity error occurred")

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'successful'}


@router.put("/update")
async def update_task(task_id: int, task_update: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    query = update(Task).where(Task.id == task_id).values(
        title=task_update.title,
        content=task_update.content,
        priority=task_update.priority
    )

    result = db.execute(query)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete("/delete")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = delete(Task).where(Task.id == task_id)
    result = db.execute(query)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task DELETE is successful!'}
