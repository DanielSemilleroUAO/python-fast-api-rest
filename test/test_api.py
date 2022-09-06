from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from main import app
from app.db.models import Base
from app.db.database import get_db

db_path = os.path.join(os.path.dirname(__file__), 'test.db')
db_uri = "sqlite:///{}".format(db_path)
engine_test = create_engine(db_uri, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)
Base.metadata.create_all(bind=engine_test)

cliente = TestClient(app)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


def test_crear_usuario():
    usuario = {
        "username": "string2",
        "password": "string2",
        "nombre": "string2",
        "apellido": "string2",
        "telefono": 0,
        "correo": "string2",
        "creacion": "2022-09-06T17:25:56.971102"
    }
    response = cliente.post('/user', json=usuario)
    assert response.status_code == 201

    usuario = {
        "username": "string2",
        "password": "string2"
    }
    response_token = cliente.post('/login', data=usuario)
    assert response_token.status_code == 200
    assert response_token.json()['token_type'] == 'bearer'

    headers = {
        'Authorization': f'Bearer {response_token.json()["access_token"]}'
    }

    response = cliente.get('/user', headers=headers)
    assert response.status_code == 200


def test_delete_database():
    db_path = os.path.join(os.path.dirname(__file__), 'test.db')
    os.remove(db_path)
