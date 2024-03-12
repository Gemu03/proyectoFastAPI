from fastapi import APIRouter, HTTPException
from typing import List
from app.base_de_datos import engine, SessionLocal, Base
from app.modelos.perfil import Perfil, PerfilCreate

router = APIRouter()


@router.post("/perfiles/", response_model=Perfil)
async def crear_perfil(perfil: PerfilCreate):
    # Aquí iría la lógica para crear un nuevo perfil en la base de datos
    pass


@router.get("/perfiles/", response_model=List[Perfil])
async def obtener_perfiles():
    # Aquí iría la lógica para obtener todos los perfiles de la base de datos
    pass


@router.get("/perfiles/{perfil_id}", response_model=Perfil)
async def obtener_perfil(perfil_id: int):
    # Aquí iría la lógica para obtener un perfil específico de la base de datos
    pass
