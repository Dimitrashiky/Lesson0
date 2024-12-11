from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root() -> str:
    return "Главная страница"

@app.get('/user/admin')
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user(user_id: int) -> str:
    return f"Вы вошли как пользователь №{user_id}"

@app.get("/user")
async def nicK_age(username: str, age: int):
    return f"Информация о пользователе. Имя:{username}, Возраст:{age}"