from pydantic import BaseModel

class HomeBase(BaseModel):
    description: str
    addres: str


class HomeCreate(HomeBase):
    pass


class HomeUpdate(HomeBase):
    id: int
