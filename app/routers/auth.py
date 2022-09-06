from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import Login
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.repository import auth
from app.db import models
from app.repository import user
from typing import List

router = APIRouter(
    prefix='/login',
    tags=['Login']
)


@router.post('', status_code=status.HTTP_200_OK)
def login(login: Login, db: Session = Depends(get_db)):
    auth.auth_user(login, db)
    return {'test': 'test'}

