import uvicorn
from fastapi import FastAPI
from core.config import settings
from core.models import db

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, 
                host=settings.run.host, port=settings.run.port)