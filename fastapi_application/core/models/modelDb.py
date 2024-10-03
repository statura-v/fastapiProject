from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, Boolean, text, Table, Column, Float
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
                   Column("id", Integer, autoincrement=True, index=True), 
                   Column("user_id", Integer, ForeignKey("user.id")), 
                   Column("home_id", Integer, ForeignKey("home.id")))

role_users = Table('role_users', Base.metadata,
                   Column("id", Integer, autoincrement=True, index=True), 
                   Column("user_id", Integer, ForeignKey("user.id")),
                   Column("role_id", Integer, ForeignKey("role.id")))

return_result_device = Table('return_result_device', Base.metadata,
                Column("id", Integer, autoincrement=True, index=True), 
                Column("return_result_id", Integer, ForeignKey("return_device.id")),
                Column("value_format_id", Integer, ForeignKey("device_value_format.id")))

command_devices = Table('command_devices', Base.metadata,
                Column("id", Integer, autoincrement=True, index=True), 
                Column("return_device_id", Integer, ForeignKey("return_device.id")),
                Column("execution_device_id", Integer, ForeignKey("execution_device.id")),
                Column("command_id", Integer, ForeignKey("command.id")))


class User(Base):
    __tablename__= "user"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hashed_password: Mapped[str] = mapped_column(String(256))
    first_name: Mapped[str] = mapped_column(String(256)) 
    last_name: Mapped[str] = mapped_column(String(256))
    number_telephone: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(256))

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
    description: Mapped[str] = mapped_column(Text, nullable=True)
    address: Mapped[str] = mapped_column(String(256))

    returnDevices: Mapped[List['ReturnDevice']] = relationship("ReturnDevice", back_populates="home")
    executionDevices: Mapped[List['ExecutionDevice']] = relationship("ExecutionDevice", back_populates="home")
    users: Mapped[List['User']] = relationship(secondary=home_users)


class DeviceType(Base):
    __tablename__ = "device_type"

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] =mapped_column(Text)


    returnDevices: Mapped[List['ReturnDevice']] = relationship("RetunDevices", back_populates="device_type")
    executionDevices: Mapped[List['ExecutionDevice']] = relationship("ExecutionDevice", back_populates="device_type")


class ReturnDevice(Base):
    __tablename__ = "return_device"

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(Text)
    addres: Mapped[str] = mapped_column(String(256))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("device_type.id"))
    home_id: Mapped[int] = mapped_column(Integer, ForeignKey("home.id"))

    home: Mapped[Home] = relationship("Home", back_populates="return_device") 
    deviceType: Mapped[DeviceType] = relationship("DeviceType", back_populates="return_device")
    
    command: Mapped[List["Command"]] = relationship(secondary=command_devices)
    returnResult: Mapped[List["DeviceValueFormat"]] = relationship(secondary=command_devices)


class ExecutionDevice(Base):
    __tablename__ = 'execution_device'

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(Text)
    addres: Mapped[str] = mapped_column(String(256))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("device_type.id"))
    home_id: Mapped[int] = mapped_column(Integer, ForeignKey("home.id"))

    deviceType: Mapped[DeviceType] = relationship("DeviceType", back_populates="execution_device")
    home: Mapped[Home] = relationship("Home", back_populates="execution_device")
    command: Mapped[List["Command"]] = relationship(secondary=command_devices)


class DeviceValueFormat(Base):
    __tablename__ = 'device_value_format'

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    textValue:Mapped[str] =  mapped_column(String(64), nullable=True)
    floatValue: Mapped[float] = mapped_column(Float, nullable=True)

    returnDevice: Mapped[List["ReturnDevice"]] = relationship(secondary=return_result_device)


class Command(Base):
    __tablename__ = 'command'

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    command: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(Text)

    returnDevice: Mapped[List["ReturnDevice"]] = relationship(secondary=command_devices)
    executionDevices: Mapped[List['ExecutionDevice']] = relationship(secondary=command_devices)
    



























    