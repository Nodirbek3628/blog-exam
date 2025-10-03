# engine, LocalSession, Base larni yarating
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import config


url = URL.create(
    drivername="postgresql+psycopg2",
    host=config.DB_HOST,
    port=config.DB_PORT,
    username=config.DB_USER,
    password=config.DB_PASS,
    database=config.DB_NAME
)

engine = create_engine(url)

Base = declarative_base()

LocalSession = sessionmaker(engine)

