from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime, Text, Boolean, text, Table, Column, Float
from typing import Annotated, List
import datetime

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
    __tablename__ = "user"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hashed_password: Mapped[str] = mapped_column(String(256))
    first_name: Mapped[str] = mapped_column(String(256)) 
    last_name: Mapped[str] = mapped_column(String(256))
    number_telephone: Mapped[str] = mapped_column(String(256))
    email: Mapped[str] = mapped_column(String(256))

    homes: Mapped[List['Home']] = relationship("Home", secondary=home_users, overlaps="users")
    roles: Mapped[List['Role']] = relationship("Role", secondary=role_users, overlaps="roles")

class Role(Base):
    __tablename__ = "role"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    role_name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text, nullable=True)

    users: Mapped[List['User']] = relationship("User", secondary=role_users, overlaps="roles")

class Home(Base):
    __tablename__ = "home"

    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    address: Mapped[str] = mapped_column(String(256))

    returnDevices: Mapped[List['ReturnDevice']] = relationship("ReturnDevice", back_populates="home")
    executionDevices: Mapped[List['ExecutionDevice']] = relationship("ExecutionDevice", back_populates="home")
    users: Mapped[List['User']] = relationship("User", secondary=home_users, overlaps="homes")

class DeviceType(Base):
    __tablename__ = "device_type"

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128))
    description: Mapped[str] = mapped_column(Text)
    returnDevices: Mapped[List['ReturnDevice']] = relationship("ReturnDevice", back_populates="deviceType")
    executionDevices: Mapped[List['ExecutionDevice']] = relationship("ExecutionDevice", back_populates="deviceType")

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

    home: Mapped[Home] = relationship("Home", back_populates="returnDevices") 
    deviceType: Mapped[DeviceType] = relationship("DeviceType", back_populates="returnDevices")
    commands: Mapped[List["Command"]] = relationship(secondary=command_devices, overlaps="returnDevices")
    returnResults: Mapped[List["DeviceValueFormat"]] = relationship(secondary=return_result_device, overlaps="commands,executionDevices")

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

    deviceType: Mapped[DeviceType] = relationship("DeviceType", back_populates="executionDevices")
    home: Mapped[Home] = relationship("Home", back_populates="executionDevices")
    commands: Mapped[List["Command"]] = relationship(secondary=command_devices, overlaps="commands, returnDevices")


class DeviceValueFormat(Base):
    __tablename__ = 'device_value_format'

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    textValue: Mapped[str] = mapped_column(String(64), nullable=True)
    floatValue: Mapped[float] = mapped_column(Float, nullable=True)

    returnDevices: Mapped[List["ReturnDevice"]] = relationship(secondary=return_result_device, overlaps="returnResults")

class Command(Base):
    __tablename__ = 'command'

    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    command: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(Text)

    returnDevices: Mapped[List["ReturnDevice"]] = relationship(secondary=command_devices, overlaps="commands,executionDevices")
    executionDevices: Mapped[List['ExecutionDevice']] = relationship(secondary=command_devices, overlaps="commands,returnDevices")

Base.registry.configure()