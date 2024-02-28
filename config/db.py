from sqlalchemy import create_engine, MetaData

metadata = MetaData()

engine = create_engine("mysql+pymysql://admin:Cod79022023b!@localhost:3306/financedb")

connection = engine.connect()