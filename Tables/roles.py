from sqlalchemy import (
    Table,
    Column,
    String,
    Integer
)
from Database.metadata import metadata
from Tables.BaseModel import BaseModel

roles_table = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('role', String(256), nullable=False)
)


role = BaseModel(roles_table)