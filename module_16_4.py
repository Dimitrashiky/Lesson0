from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel, Field



app = FastAPI()




class User(BaseModel):
    id: int
    username: str
    age: int
users: List[User] = []

class UserPost(BaseModel):
    username: str = Field(..., min_length= 4, max_length= 20, description= "Enter User Name", example= "Lucian")
    age: int = Field(..., ge= 18, le= 120, description= "Enter Age", example="24")

@app.get("/")
async def root() -> str:
    return "Главная страница"


@app.get("/users", response_model= List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model= User)
async def create_users(nameage: UserPost):
    user_id = max((i.id for i in users), default= 0) + 1
    user = User(id = user_id, username= nameage.username, age= nameage.age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, nameage: UserPost):
    for i in users:
        if user_id == i.id:
            i.username = nameage.username
            i.age = nameage.age
            return i
    raise HTTPException(status_code= 404, detail= "User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge= 1, description="Enter User id", example= 1)]):
    for i, j in enumerate(users):
        if j.id == user_id:
           return users.pop(i)

    raise HTTPException(status_code= 404, detail= "User was not found")







