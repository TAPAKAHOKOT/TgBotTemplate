from sqlalchemy import (
    ForeignKey,
    Table,
    Column,
    String,
    Integer
)
from Database.metadata import metadata
from Tables.BaseModel import BaseModel

users_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(256), nullable=True, unique=True),
    Column('role_id', ForeignKey('roles.id'), nullable=False)
)


user = BaseModel(users_table)