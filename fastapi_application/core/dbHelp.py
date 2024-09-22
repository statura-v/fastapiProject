from fastapi_application.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

DATABASE_URL = f'postgresql+asyncpg://{str(settings.db_user)}:{str(settings.db_pass)}@{str(settings.db_host)}:{str(settings.db_port)}/{str(settings.db_name)}'

class BaseDatabaseConnector:
    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url, echo=True)
        self.async_session_maker = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)
    
    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            yield session

db = BaseDatabaseConnector(database_url=DATABASE_URL)