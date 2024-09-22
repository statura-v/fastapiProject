from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, Boolean, text
from typing import Annotated
import datetime


intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))]
updated_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("CURRENT_TIMESTAMP"),
    onupdate=text("CURRENT_TIMESTAMP")
)]
str_256 = Annotated[str, 256]
str256 = Annotated[str_256, mapped_column(nullable=False)]


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__= "user"

    __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    hashed_password: Mapped[str256]
    firstName: Mapped[str256]
    lastName: Mapped[str256]
    numberTelephone: Mapped[str256]
    createdAt: Mapped[created_at]
    updatedAt:Mapped[updated_at]
    roleId = mapped_column(ForeignKey('role.id'))

    role = relationship("Role", uselist=False, back_populates="user")

class Role(Base):
    __tablename__ = "role"

    __table_args__ = {'extend_existing': True}

    id: Mapped[intpk]
    roleName: Mapped[str256]

    user = relationship("User", uselist=False, back_populates="role")




    