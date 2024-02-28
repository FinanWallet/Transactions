from sqlalchemy import create_engine, Metadata

engine = create_engine("mysql://root:root@localhost:3306/financeun")

meta = Metadata()

connection = engine.connect()