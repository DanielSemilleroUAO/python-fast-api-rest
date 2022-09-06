from fastapi import FastAPI
import uvicorn
from app.routers import user, auth
from app.db.database import Base, engine


def create_table():
    Base.metadata.create_all(bind=engine)


# create_table()


app = FastAPI()
app.include_router(router=user.router)
app.include_router(router=auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
