from pydantic import BaseModel

class RoleBase(BaseModel):
    role_name: str
    decription: str


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    id: int
    