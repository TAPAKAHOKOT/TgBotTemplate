from sqlalchemy import (
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

class Role(Base, BaseModel):
    __tablename__ = 'roles'
    metadata=metadata

    id = Column(Integer, autoincrement=True, primary_key=True)
    role = Column(String(256), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))
    updated_at = Column(DateTime, default=datetime.utcnow, server_default=text('now()'))


    def get_class(self):
        return Role