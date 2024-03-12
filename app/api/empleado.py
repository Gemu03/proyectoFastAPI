from fastapi import APIRouter, HTTPException
from typing import List
from app.base_de_datos import engine, SessionLocal, Base
from app.modelos.empleado import Empleado, EmpleadoCreate

router = APIRouter()


@router.post("/empleados/", response_model=Empleado)
async def crear_empleado(empleado: EmpleadoCreate):
    return empleado
    pass


@router.get("/empleados/", response_model=List[Empleado])
async def obtener_empleados():
    return []
    pass


@router.get("/empleados/{empleado_id}", response_model=Empleado)
async def obtener_empleado(empleado_id: int):
    return {"id": empleado_id, "nombre": "Juan", "apellido": "Pérez", "email": "juanperez@hotmail.com"}
    pass
