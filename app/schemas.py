from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# User Model
class User(BaseModel):
    username: str
    password: str
    nombre: str
    apellido: Optional[str]
    telefono: int
    correo: str
    creacion: datetime = datetime.now()


class UpdateUser(BaseModel):
    username: str = None
    password: str = None
    nombre: str = None
    apellido: Optional[str] = None
    telefono: int = None
    correo: str = None
    creacion: datetime = None


class ResponseUser(BaseModel):
    id: int
    username: str
    nombre: str
    apellido: Optional[str]
    telefono: int

    class Config():
        orm_mode = True


class UserId(BaseModel):
    id: int


class Login(BaseModel):
    username: str
    password: str
