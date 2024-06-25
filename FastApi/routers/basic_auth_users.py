# Para arrancar el servidor uvicorn users:app --reload
# ?Instala FastApi: pip install "fastapi[all]"

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# !Entidad user
class User(BaseModel):
    username: str
    full_name: str
    email: str
    diabled: bool

# !Entidad Pass
class UserDB(User):
    password: str
    
# !Base de datos Simulada
users_db = {
    "santi": {
        "username": "santi",
        "full_name": "Santi Luque Torrejon",
        "email": "santi@gmail.com",
        "diabled": False,
        "password": "123456"
        },
    "david": {
        "username": "david",
        "full_name": "David Corral Plaza",
        "email": "david@gmail.com",
        "diabled": True,
        "password": "654321"
        }
}

# !Funcion

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# !Depends

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticacion invalidas", headers={"WWW-Autenticate":"Bearer"})
    if user.diabled:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Usuario Inactivo", headers={"WWW-Autenticate":"Bearer"})
    return user
        


# !Autenticacion

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El Usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/user/me")
async def me(user: User = Depends(current_user)):
    return user
    


    

    