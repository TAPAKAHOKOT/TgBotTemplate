from curses import meta
from sqlalchemy import (
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

class Role(Base, BaseModel):
    __tablename__ = 'roles'
    metadata=metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role = Column(String(256), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))


    def get_class(self):
        return Role