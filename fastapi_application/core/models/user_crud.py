from sqlalchemy.orm import Session
from core.dbHelp import db
from core.models.modelDb import User
from core.schemas.user_schemas import UserCreate, UserUpdate


def get_user_by_id(database: Session, user_id: int):
    return database.query(User).get(user_id)


def delete_user_by_id(database: Session, user_id: int):
    user = database.query(User).get(user_id)
    database.delete(user)
    database.commit()
    return {'Status': 200}


def create_user(database: Session, schema: UserCreate): 
    user = User(first_name = schema.first_name,
                last_name = schema.last_name,
                email = schema.email,
                hashed_password = schema.hashed_password,
                number_telephone = schema.number_telephone
                )
    database.add(user)
    database.commit()
    return {"Status" : 200}

def update_user(database: Session, schema: UserUpdate, user_id: int):
    user = database.query(User).get(user_id)
    user.first_name = schema.first_name
    #добисать все поля. 
    database.commit()
    database.refresh(user)
    return {'Status': 200}