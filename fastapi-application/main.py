import uvicorn
from fastapi import FastAPI
from core.config import runConfig

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, 
                host=runConfig.host, port=runConfig.port)