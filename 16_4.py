from fastapi import FastAPI, HTTPException, status, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

users =[]

class User(BaseModel):
    id: int = None
    username: str = None
    age: int = None


@app.get('/users')
async def get_all_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int) -> str:
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_user} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")