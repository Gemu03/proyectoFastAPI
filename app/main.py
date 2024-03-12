from fastapi import FastAPI
from app.api import empleado, perfil

app = FastAPI()

app.include_router(empleado.router, prefix="/api", tags=["empleados"])
app.include_router(perfil.router, prefix="/api", tags=["perfiles"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
