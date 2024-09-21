from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class DataBaseSettings(BaseModel):
    url: PostgresDsn
    echo: bool = False 
    echo_pool: bool = False
    max_overflow: int = 10 
    pool_size: int = 50

class Settings(BaseSettings):
    modelConfig: SettingsConfigDict = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__",
        env_file=".env"
    )
    runConfig: RunConfig = RunConfig()
    db: DataBaseSettings

settings = Settings()



