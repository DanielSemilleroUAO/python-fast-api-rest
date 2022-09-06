from fastapi import APIRouter, Depends, status, HTTPException
from app.schemas import User, UserId, ResponseUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from app.repository import user
from typing import List

root_path = '/users'

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.get('', response_model=List[ResponseUser], status_code=status.HTTP_200_OK)
def get_all_users(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    return data


@router.post('', status_code=status.HTTP_201_CREATED)
def create_users(usuario: User, db: Session = Depends(get_db)):
    try:
        user.create_user(usuario, db)
        return {'message': 'user created'}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Error creando usuario')


@router.get('/{user_id}', response_model=ResponseUser)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.get_user_by_id(user_id, db)


@router.post('/body')
def get_user_by_id_json(user_id: UserId, db: Session = Depends(get_db)):
    return user.get_user_by_id(user_id.id, db)


@router.delete('/{user_id}')
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return user.delete_user_by_id(user_id, db)


@router.patch('')
def update_user_by_id(user_id: int, new_user: UpdateUser, db: Session = Depends(get_db)):
    return user.update_user_by_id(user_id, new_user, db)


@router.put('/{user_id}')
def delete_user_by_id(user_id: int, new_user: User, db: Session = Depends(get_db)):
    return user.update_user_by_id(user_id, new_user, db)
