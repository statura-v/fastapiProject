from fastapi import APIRouter, Depends, HTTPException
from core.schemas.user_schemas import UserCreate, UserUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from core.db_help import db
from core.models.user_crud import create_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["Works with User"])

@router.post('/')
async def create_new_user(user: UserCreate, session: AsyncSession = Depends(db.get_async_session)):
    try:
        print("Start")
        created_user = await create_user(session, user)
        print("End", created_user)
        return created_user
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    
@router.get("/{user_id}")
async def return_user_by_id(user_id: int, session: AsyncSession = Depends(db.get_async_session)):
    try:
        current_user = await get_user_by_id(session, user_id)
        if not current_user:
            raise HTTPException(status_code=404, detail="User not found")
        return current_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))