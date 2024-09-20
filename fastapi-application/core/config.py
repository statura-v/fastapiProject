from pydantic import BaseModel

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

runConfig = RunConfig()
