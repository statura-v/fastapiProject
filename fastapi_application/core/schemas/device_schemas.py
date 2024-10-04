from pydantic import BaseModel

class ReturnDeviceBase(BaseModel):
    name: str
    user_id: int
    type_id: int
    description: str
    addres: str


class ReturnDeviceCreate(ReturnDeviceBase):
    pass


class ReturnDeviceUpdate(ReturnDeviceBase):
    id: int


class ExecutionDeviceCreate(ReturnDeviceBase):
    pass


class ExecutionDeviceUpdate(ReturnDeviceUpdate):
    pass


#Встал вопрос а как валидировать связь Мany to Many


