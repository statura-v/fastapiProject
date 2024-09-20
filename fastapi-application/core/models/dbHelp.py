from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from core.config import Settings

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
    url=str(Settings.db.url),
    echo=Settings.db.echo,
    echo_pool=Settings.db.echo_pool,
    max_overflow=Settings.db.max_overflow,
    pool_size=Settings.db.pool_size
)
