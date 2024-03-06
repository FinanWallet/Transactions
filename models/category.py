from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from config.db import metadata, engine

meta = MetaData()

categories = Table('category', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)))
metadata.create_all(engine)