from sqlalchemy import Table, Column, Integer, String, MetaData, insert
from config.db import metadata, engine

meta = MetaData()

categories = Table('category', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)))
metadata.create_all(engine)

# Insertar categorías por defecto
# with engine.connect() as connection:
#     connection.execute(insert(categories), [
#         {"name": "Obligations"},
#         {"name": "Game"},
#         {"name": "Food"},
#         {"name": "Savings"},
#     ])