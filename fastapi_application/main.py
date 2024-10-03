import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import Session
from core import session_local
from core.config import settings

app = FastAPI()

def get_db():
    db = session_local()
    try:
        yield db    #почему ?
    finally:
        db.close()


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, 
                host=settings.run.host, port=settings.run.port)