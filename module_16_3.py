from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {"1": "Имя: Example, возраст: 18"}

@app.get("/")
async def root() -> str:
    return "Главная страница"


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_users(username: Annotated[str, Path(min_length= 4, max_length= 20, description="Enter Username", example="UrbanUser")], age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= "24")]) -> str:
    user_id = str(int(max(users.keys())) + 1)
    users.update({user_id: f"Имя: {username}, возраст: {age}"})
    return f"User {user_id} is registrated"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge= 1, description="Enter User id", example= 1)],
                      username: Annotated[str, Path(min_length= 4, max_length= 20, description="Enter Username", example="UrbanUser")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter age", example= "24")]) -> str:
    if str(user_id) in users:
        users[str(user_id)] = f"Имя: {username}, возраст: {age}"
        return f"The user {user_id} is updated"
    else: return "User is not found"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge= 1, description="Enter User id", example= 1)]):
    if str(user_id) in users:
        del users[str(user_id)]
        return f"User {user_id} has been deleted"
    else:
        return "User is not found"




