from fastapi import FastAPI

# from sqlalchemy.orm import Session
# from core import session_local
from core.config import settings

from core import db
from core.routers import router_user


app = FastAPI(title="Home Helper")

app.include_router(router_user)


async def get_db():
    async for session in db.get_async_session():
        try:
            yield session
        finally:
            await session.close()
