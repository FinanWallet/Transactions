from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
from config.db import metadata, engine

meta = MetaData()

records = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('date', DateTime), 
               Column('description', String(50)), 
               Column('amount', Float),
               Column('account', Integer, ForeignKey('account.id')), 
               Column('category', Integer, ForeignKey('category.id')),
               Column('subcategory', Integer, ForeignKey('subcategory.id')),
               Column('payment_method', Integer, ForeignKey('payment_method.id')))

metadata.create_all(engine)