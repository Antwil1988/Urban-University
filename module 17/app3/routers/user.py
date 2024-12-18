from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel

# Создаем экземпляр APIRouter с префиксом и тегом
router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Pydantic-схема UserResponse: Определяет порядок полей, который будет соблюдаться при формировании JSON-ответа.
class UserResponse(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str


@router.get("/", response_model=list[UserResponse])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    query = select(User)
    result = db.scalars(query).all()
    return result


@router.get("/user_id")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    result = db.scalars(query).first()

    if result is not None:
        return result
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@router.post("/create")
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = insert(User).values(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)
    )

    try:
        db.execute(new_user)
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'successful'}
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="User with this ID or username already exists")


@router.put("/update")
async def update_user(user_id: int, user_update: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    query = update(User).where(User.id == user_id).values(
        firstname=user_update.firstname,
        lastname=user_update.lastname,
        age=user_update.age,
    ).execution_options(synchronize_session="fetch")
    # Обеспечивает синхронизацию сессии после выполнения запроса.



    result = db.execute(query)
    db.commit()

    if result.rowcount == 0:
        # Проверяет, была ли обновлена хотя бы одна запись.
        raise HTTPException(status_code=404, detail="User was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.get("/{user_id}/tasks")
async def user_tasks(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Проверка существования пользователя
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")

    # Получение всех задач пользователя
    tasks = db.query(Task).filter(Task.user_id == user_id).all()

    return tasks


@router.delete("/delete")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    # Удаление всех задач, связанных с пользователем
    task_query = delete(Task).where(Task.user_id == user_id)
    db.execute(task_query)

    # Удаление пользователя
    user_query = delete(User).where(User.id == user_id)
    result = db.execute(user_query)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="User was not found")

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User DELETE is successful!'}
