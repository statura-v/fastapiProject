from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, Boolean, text, Table, Column
from typing import Annotated, List
import datetime


# intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
# created_at = Annotated[datetime.datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))]
# updated_at = Annotated[datetime.datetime, mapped_column(
    # server_default=text("CURRENT_TIMESTAMP"),
    # onupdate=text("CURRENT_TIMESTAMP")
# # )]

# str_256 = Annotated[str, 256]
# str256 = Annotated[str_256, mapped_column(nullable=False)]


class Base(DeclarativeBase):
    created_at = mapped_column(DateTime)
    updated_at = mapped_column(DateTime)


home_users = Table('home_users', Base.metadata, 
                   Column("user_id", Integer, ForeignKey("user.id")), 
                   Column("home_id", Integer, ForeignKey("home.id")))

role_users = Table('role_users', Base.metadata,
                   Column("user_id", Integer, ForeignKey("user.id")),
                   Column("role_id", Integer, ForeignKey("role.id")))


class User(Base):
    __tablename__= "user"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hashed_password: Mapped[str] = mapped_column(String(256))
    first_name: Mapped[str] = mapped_column(String(256)) 
    last_name: Mapped[str] = mapped_column(String(256))
    number_telephone: Mapped[str] = mapped_column(String(256))

    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))

    homes: Mapped[List['Home']] = relationship(secondary=home_users)
    roles: Mapped[List['Role']] = relationship(secondary=role_users)


class Role(Base):
    __tablename__ = "role"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String(256))

    users: Mapped[List['User']] = relationship(secondary=role_users)


class Home(Base):
    __tablename__ = "home"

    __table_args__= {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    home_name: Mapped[str] = mapped_column(String(256))
    addres: Mapped[str] = mapped_column(String(256), nullable=True)

    users: Mapped[List['User']] = relationship(secondary=home_users)










    