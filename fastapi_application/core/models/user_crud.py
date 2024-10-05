# from sqlalchemy.orm import Session
# from fastapi_application.core.db_help import db
# from fastapi_application.core.models.model_db import User
# from core.schemas.user_schemas import UserCreate, UserUpdate


# def get_user_by_id(database: Session, user_id: int):
#     return database.query(User).get(user_id)


# def delete_user_by_id(database: Session, user_id: int):
#     user = database.query(User).get(user_id)    
#     database.delete(user)
#     database.commit()
#     return user


# def create_user(database: Session, schema: UserCreate): 
#     user = User(first_name = schema.first_name,
#                 last_name = schema.last_name,
#                 email = schema.email,
#                 hashed_password = schema.hashed_password,
#                 number_telephone = schema.number_telephone
#                 )
#     database.add(user)
#     database.commit()
#     return user



# def update_user(database: Session, schema: UserUpdate, user_id: int):
#     user = database.query(User).get(user_id)

#     user.first_name = schema.first_name
#     user.last_name = schema.last_name
#     user.email = schema.email
#     user.hashed_password = schema.hashed_password
#     user.number_telephone = schema.number_telephone
    
#     database.commit()
#     database.refresh(user)
#     return user

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, select, insert
from core.models.model_db import User
from core.schemas.user_schemas import UserCreate, UserUpdate

async def get_user_by_id(database: AsyncSession, user_id: int):
    result = await database.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def delete_user_by_id(database: AsyncSession, user_id: int):
    result = await database.execute(delete(User).where(User.id == user_id))
    await database.commit()
    return result.rowcount > 0

async def create_user(session: AsyncSession, schema: UserCreate):
    stmt = insert(User).values(**schema.dict())
    await session.execute(stmt)
    await session.commit()
    return {"Status": 200}


async def update_user(database: AsyncSession, schema: UserUpdate, user_id: int):
    result = await database.execute(
        update(User)
        .where(User.id == user_id)
        .values(**schema.dict())
    )
    await database.commit()
    return result.rowcount > 0