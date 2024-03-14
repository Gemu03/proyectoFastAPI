from fastapi import APIRouter, HTTPException, Depends
from typing import List

from sqlalchemy.orm import Session

from app.base_de_datos import engine, SessionLocal, Base
from app.modelos.empleado import Empleado, EmpleadoCreate
from app.base_de_datos import get_db

router = APIRouter()


@router.post("/empleados/", response_model=Empleado)
async def crear_empleado(empleado: EmpleadoCreate):

    db=SessionLocal()
    nuevo_empleado=Empleado(**empleado.dict())
    db.add(nuevo_empleado)
    db.commit()
    db.close()

    return nuevo_empleado

@router.get("/empleados/todos", response_model=List[Empleado])
async def obtener_empleados(db: Session = Depends(get_db)):
    empleados = db.query(Empleado).all()
    return empleados


@router.get("/empleados/{empleado_id}", response_model=Empleado)
async def perfil_empleado(empleado_id: int):
    return {"id": empleado_id, "nombre": "Juan", "apellido": "Pérez", "email": "juanperez@hotmail.com"}
