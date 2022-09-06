from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import Login
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.repository import auth
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/login',
    tags=['Login']
)


@router.post('', status_code=status.HTTP_200_OK)
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    auth_response = auth.auth_user(login, db)
    return auth_response
