from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float
from config.db import metadata, engine

meta = MetaData()

categories = Table('category', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(255)), 
               Column('limit', Float),
               Column('account', Integer, ForeignKey('account.id')))

metadata.create_all(engine)