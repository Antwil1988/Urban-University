from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_user(
    username: Annotated[str, Path(min_length=5, max_length=50)],
    age: Annotated[int, Path(ge=18, le=120)]) -> str:
    
    # Находим максимальный ключ в словаре и увеличиваем его
    max_key = max(map(int, users.keys()), default=0) + 1
    user_id = str(max_key)
    
    # Добавляем нового пользователя в словарь
    users[user_id] = f"Имя: {username}, возраст: {age}"
    
    # Возвращаем сообщение с подтверждением
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: str,
    username: Annotated[str, Path(min_length=1, max_length=50)],
    age: Annotated[int, Path(ge=18, le=120)]) -> str:

    # Проверяем, существует ли user_id в словаре
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Обновляем пользователя в словаре
    users[user_id] = f"Имя: {username}, возраст: {age}"
    
    # Возвращаем сообщение с подтверждением
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    # Проверяем, существует ли user_id в словаре
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Удаляем пользователя из словаря
    del users[user_id]
    
    # Возвращаем сообщение с подтверждением
    return f"The user {user_id} has been deleted"



