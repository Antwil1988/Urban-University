from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/')
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}')
async def get_user_page(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


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
