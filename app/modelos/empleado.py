from pydantic import BaseModel


class EmpleadoBase(BaseModel):
    nombre: str
    apellido: str
    email: str


class EmpleadoCreate(EmpleadoBase):
    pass


class Empleado(EmpleadoBase):
    id: int

    class Config:
        orm_mode = True
