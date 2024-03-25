from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from config.db import metadata, engine

meta = MetaData()

accounts = Table('account', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(50)))
metadata.create_all(engine)