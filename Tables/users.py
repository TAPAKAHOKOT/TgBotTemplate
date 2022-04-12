from importlib_metadata import metadata
from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    String,
    Integer,
    DateTime,
    text
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from Database.metadata import metadata
from Tables.BaseModel import BaseModel

Base = declarative_base()

class User(Base, BaseModel):
    __tablename__ = 'users'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(ForeignKey('roles.id'), nullable=True)

    chat_id = Column(Integer, nullable=False, unique=True)
    username = Column(String(256), nullable=True, unique=True)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))


    def get_class(self):
        return User