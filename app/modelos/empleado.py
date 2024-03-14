from pydantic import BaseModel



class EmpleadoBase(BaseModel):
    id: int
    nombre: str
    edad: str
    correo: str
    rol: str


class EmpleadoCreate(EmpleadoBase):
    pass


class Empleado(EmpleadoBase):
    id: int

    class Config:
        orm_mode = True
