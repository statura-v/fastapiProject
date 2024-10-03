from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    hashed_password: str
    number_telephone: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int