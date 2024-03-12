from pydantic import BaseModel


class PerfilBase(BaseModel):
    habilidades: str
    experiencia: int


class PerfilCreate(PerfilBase):
    pass


class Perfil(PerfilBase):
    id: int

    class Config:
        orm_mode = True