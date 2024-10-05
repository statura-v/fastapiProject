from fastapi import APIRouter, Depends, HTTPException
from core.schemas.user_schemas import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_help import db
from core.models.user_crud import create_user

router = APIRouter(prefix="/users", tags=["Работа с пользователями"])

@router.post('/')
async def create_new_user(user: UserCreate, session: AsyncSession = Depends(db.get_async_session)):
    try:
        print("Start______________")
        created_user = await create_user(session, user)
        print("__________End + ", created_user)
        return created_user
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))