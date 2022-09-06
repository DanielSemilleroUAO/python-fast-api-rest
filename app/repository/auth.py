from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import User, UpdateUser, Login
from app.db import models
from passlib.context import CryptContext
from app.token import create_access_token


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def auth_user(usuario: Login, db: Session):
    user = db.query(models.User).filter(models.User.username == usuario.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='El usuario no existe')
    if not pwd_context.verify(usuario.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username or password incorrect')
    access_token = create_access_token(
        data={"sub": usuario.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}
