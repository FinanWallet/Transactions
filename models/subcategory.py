# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, insert
# from config.db import metadata, engine

# meta = MetaData()

# subcategories = Table('subcategory', metadata, Column('id', Integer, primary_key=True), 
#                Column('name', String(50)), 
#                Column('category_id', Integer, ForeignKey('category.id')))

# metadata.create_all(engine)