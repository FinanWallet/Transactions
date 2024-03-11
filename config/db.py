from sqlalchemy import create_engine, MetaData
from config.config import settings

metadata = MetaData()

engine = create_engine(settings.DB_URL)

connection = engine.connect()