import uvicorn
from fastapi import FastAPI
from core.config import Settings

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, 
                host=Settings.runConfig.host, port=Settings.runConfig.port)