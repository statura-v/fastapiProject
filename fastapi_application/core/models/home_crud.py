from sqlalchemy.orm import Session
from fastapi_application.core.db_help import db
from fastapi_application.core.models.model_db import Home
from core.schemas.home_schemas import HomeCreate, HomeUpdate

def get_home_by_id(database: Session, home_id: int):
    return database.query(Home).get(home_id)


def create_home(database: Session, schema: HomeCreate):
    home = Home(description=schema.description,
                addres=schema.addres)
    database.add(home)
    database.commit()
    return {"Status" : 200, "Message": "Success"}


def delete_home_by_id(database: Session, home_id: int):
    home = database.query(Home).get(home_id)
    if not home:
        return {'Status': 404, 'Message': 'Home not found'}
    database.delete(home)
    database.commit()
    return {"Status" : 200, "Message": "Success"}


def update_home(database: Session, schema: HomeUpdate, home_id: int):
    home = database.query(Home).get(home_id)
    if not home:
       return {'Status': 404, 'Message': 'Home not found'}
    home.description = schema.description
    home.addres = schema.addres
    database.commit()
    database.refresh(home)

    return {'Status': 200, 'Message': 'Home updated successfully'}



