from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from config.db import metadata, engine

meta = MetaData()

subcategories = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('name', String(255)), 
               Column('account', Integer, ForeignKey('account.id')), 
               Column('category', Integer, ForeignKey('category.id')))

metadata.create_all(engine)