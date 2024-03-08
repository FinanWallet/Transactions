from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
from config.db import metadata, engine

meta = MetaData()

records = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('user_id', Integer),
               Column('account_id', Integer, ForeignKey('account.id')),
               Column('subcategory_id', Integer, ForeignKey('subcategory.id')),
               Column('date', DateTime), 
               Column('amount', Float),
               Column('description', String(50)))

metadata.create_all(engine)