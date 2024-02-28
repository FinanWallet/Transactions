from sqlalchemy import Table, Column, Integer, String, MetaData, DateTime
from config.db import metadata, engine

meta = MetaData()

payment_methods = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('date', DateTime), 
               Column('name', String(255)))

metadata.create_all(engine)