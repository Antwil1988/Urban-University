from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    # Определяем id для нового пользователя
    new_id = users[-1].id + 1 if users else 1

    # Создаем нового пользователя
    new_user = User(id=new_id, username=username, age=age)

    # Добавляем пользователя в список users
    users.append(new_user)

    # Возвращаем созданного пользователя
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):

    # Поиск пользователя по user_id
    for user in users:
        if user.id == user_id:
            # Обновление данных пользователя
            user.username = username
            user.age = age
            return user

    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):

    # Поиск пользователя по user_id
    for index, user in enumerate(users):
        if user.id == user_id:
            # Удаление пользователя из списка
            deleted_user = users.pop(index)
            return deleted_user

    # Если пользователь не найден, выбрасываем исключение
    raise HTTPException(status_code=404, detail="User was not found")
