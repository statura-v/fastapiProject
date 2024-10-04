from sqlalchemy.orm import Session
from fastapi_application.core.db_help import db
from fastapi_application.core.models.model_db import User
from core.schemas.user_schemas import UserCreate, UserUpdate


def get_user_by_id(database: Session, user_id: int):
    return database.query(User).get(user_id)


def delete_user_by_id(database: Session, user_id: int):
    user = database.query(User).get(user_id)
    if not user:
        return {'Status': 404, 'Message': 'User not found'}
    
    database.delete(user)
    database.commit()
    return {'Status': 200, "Message": "User has beeb deleted"}


def create_user(database: Session, schema: UserCreate): 
    user = User(first_name = schema.first_name,
                last_name = schema.last_name,
                email = schema.email,
                hashed_password = schema.hashed_password,
                number_telephone = schema.number_telephone
                )
    database.add(user)
    database.commit()
    return {"Status" : 200, "Message": "Success"}



def update_user(database: Session, schema: UserUpdate, user_id: int):
    user = database.query(User).get(user_id)
    if not user:
        return {'Status': 404, 'Message': 'User not found'}

    user.first_name = schema.first_name
    user.last_name = schema.last_name
    user.email = schema.email
    user.hashed_password = schema.hashed_password
    user.number_telephone = schema.number_telephone
    
    database.commit()
    database.refresh(user)
    return {'Status': 200, 'Message': 'User updated successfully'}