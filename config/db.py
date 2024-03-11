from sqlalchemy import create_engine, MetaData

metadata = MetaData()

db_user = 'admin'
db_password = 'Cod79022023b!'
db_name = 'financedb'  # Make sure this database exists
db_host = 'financedb.c1ak32udummq.us-east-2.rds.amazonaws.com'
db_port = '3306'

connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(connection_string)

connection = engine.connect()