from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from config.db import metadata, engine

meta = MetaData()

accounts = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(255)), 
               Column('limit', Float))

metadata.create_all(engine)