# Para arrancar el servidor uvicorn users:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list =[User(id = 1, name = "Santi", surname = "Luque", age = 30),
            User(id = 2, name = "David", surname = "Corral", age = 30),
            User(id = 3,name = "Pepe", surname = "Pelillo", age = 55)]


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Santi", "surname": "Luque", "age": 30},
            {"name": "David", "surname": "Corral", "age": 30},
            {"name": "pepe", "surname": "Pelillo", "age": 55}]


#

@app.get("/users")
async def users():
    return users_list

#Path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
#Query

@app.get("/user/")
async def user(id: int):
    return search_user(id)
    


def search_user(id: int):
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"Error": "Usuario no encontrado"}
