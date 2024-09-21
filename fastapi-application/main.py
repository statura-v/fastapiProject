import uvicorn
from fastapi import FastAPI
from core.config import Settings
from core.models import db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    #start
    yield
    #stop
    await db.dispose()

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, 
                host=Settings.runConfig.host, port=Settings.runConfig.port)