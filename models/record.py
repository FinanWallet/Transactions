from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime, Float
from config.db import metadata

meta = MetaData()

records = Table('record', metadata, Column('id', Integer, primary_key=True), 
               Column('date', DateTime), 
               Column('description', String(255)), 
               Column('amount', Float),
               Column('account_id', Integer, ForeignKey('account.id')), 
               Column('category_id', Integer, ForeignKey('category.id')),
               Column('sub_category_id', Integer, ForeignKey('sub_category.id')),
               Column('payment_method_id', Integer, ForeignKey('payment_method.id')))

meta.create_all()