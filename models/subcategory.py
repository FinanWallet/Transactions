from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, insert
from config.db import metadata, engine

meta = MetaData()

subcategories = Table('subcategory', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)), 
               Column('category_id', Integer, ForeignKey('category.id')))

metadata.create_all(engine)

# with engine.connect() as connection:
#     connection.execute(insert(subcategories), [
#         {"name": "Lunch", "category_id": 1},
#         {"name": "Transport", "category_id": 1},
#         {"name": "Rent", "category_id": 2},
#     ])