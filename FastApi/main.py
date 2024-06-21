from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastApi!"

@app.get("/url")
async def root():
    return [{"url": "https://santidev.tecnolabs.app"}]

# Para arrancar el servidor uvicorn main:app --reload