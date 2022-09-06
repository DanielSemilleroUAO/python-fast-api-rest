from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import User, UpdateUser
from app.db import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def create_user(user: User, db: Session):
    password_hash = pwd_context.hash(user.password)
    nuevo_usuario = models.User(
        username=user.username,
        password=password_hash,
        nombre=user.nombre,
        apellido=user.apellido,
        telefono=user.telefono,
        creacion=user.creacion,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)


def get_user_by_id(user_id: int, db: Session):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El usuario no existe')
    return usuario


def delete_user_by_id(user_id: int, db: Session):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El usuario no existe')
    usuario.delete(synchronize_session=False)
    db.commit()
    return {'message': 'usuario eliminado'}


def update_user_by_id(user_id: int, new_user: UpdateUser, db: Session):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El usuario no existe')
    usuario.update(new_user.dict(exclude_unset=True))
    db.commit()
    return {'message': 'usuario actualizado'}
