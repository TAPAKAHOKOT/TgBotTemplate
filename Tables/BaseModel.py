from sqlalchemy.orm import (
    Query
)

class BaseModel:
    def __init__(self, table=None):
        self.table=table


    def get_fillable_columns(self) -> list:
        columns = self.table.columns.keys()
        columns.remove('id')

        return columns


    def check_if_lall_keys_exists(self, keys: list) -> bool:
        columns = self.get_fillable_columns()
        
        for key in keys:
            if key not in columns:
                return False
            columns.remove(key)
        return True


    def insert(self, item: dict) -> Query:
        if not self.check_if_lall_keys_exists(item.keys()):
            raise Exception(
                'Keys error', 
                'given keys: ', 
                item.keys(), 
                'fillable_columns: ', 
                self.get_fillable_columns()
            )
        
        return self.table.insert().values(**item).returning(self.table)


    def insert_many(self, items: list([dict])) -> Query:
        for item in items:
            if not self.check_if_lall_keys_exists(item.keys()):
                raise Exception(
                'Keys error', 
                'given keys: ', 
                item.keys(), 
                'fillable_columns: ', 
                self.get_fillable_columns()
            )

        return self.table.insert().values(items).returning(self.table)