from sqlalchemy import (
    ForeignKey,
    Column,
    String,
    Integer,
    DateTime,
    text
)
from sqlalchemy.orm import relationship

from datetime import datetime

from Database import Base
from Database.metadata import metadata
from Tables.BaseModel import BaseModel

class User(Base, BaseModel):
    __tablename__ = 'users'
    metadata = metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role_id = Column(ForeignKey('roles.id'), nullable=True)

    chat_id = Column(Integer, nullable=False, unique=True)
    username = Column(String(256), nullable=True, unique=True)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))

    role = relationship(
        'Role',
        lazy='select'
    )


    def get_class(self):
        return User