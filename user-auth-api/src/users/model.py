from sqlalchemy import Column, Integer, String, DateTime, MetaData, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from uuid import uuid4

from passlib.context import CryptContext

from ..config.engine import Base
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = 'users'

    meta = MetaData(schema="auth")

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username : str = Column(String, unique=True)
    pwd : str = Column(String)
    fullname: str = Column(String)
    birthdate: str= Column(String, nullable=True)
    created_at: str = Column(TIMESTAMP, server_default=func.now()) 
    updated_at: str = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()) 

    def set_password(self, password : str):
        self.pwd = pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
