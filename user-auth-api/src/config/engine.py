from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

postgres_user = os.environ.get('POSTGRES_USER')
postgres_pwd = os.environ.get('POSTGRES_PASSWORD')
postgres_db = os.environ.get('POSTGRES_DB')

DATABASE_URL = f'postgresql://postgres:postgres@localhost:5432/users'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()