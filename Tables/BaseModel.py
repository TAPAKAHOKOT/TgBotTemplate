from sqlalchemy.orm import (
    Query
)

class BaseModel:
    def get_class(self):
        return BaseModel
    

    def get_table(self):
        return self.get_class().__table__


    def insert(self, item: dict) -> Query:
        return self.get_table().insert().values(**item).returning(self.table)


    def insert_many(self, items: list([dict])) -> Query:
        return self.get_table().insert().values(items).returning(self.table)