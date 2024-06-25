# Para arrancar el servidor uvicorn users:app --reload
# ?Instala FastApi: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#!Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastApi!"

@app.get("/url")
async def root():
    return [{"url": "https://santidev.tecnolabs.app"}]

# Para arrancar el servidor uvicorn main:app --reload