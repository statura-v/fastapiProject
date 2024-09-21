from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from core.config import settings

class DataBaseHelper:
    def __init__(self, url: str, echo: bool, echo_pool: bool, max_overflow: int = 10, pool_size: int = 5) -> None:
        self.engine: AsyncEngine = create_async_engine(url=url, echo=echo, echo_pool=echo_pool, max_overflow=max_overflow, 
                                          pool_size=pool_size)
        self.sessionFactory = async_sessionmaker(bind=self.engine, autoflush=False, autocommit=False,
                                                 expire_on_commit=False)
    async def dispose(self):
        await self.engine.dispose()

    async def getSession(self):
        async with self.sessionFactory() as session:
            yield session


db = DataBaseHelper(
    url=str(settings.db.url),
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size
)
