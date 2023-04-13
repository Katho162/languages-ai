from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import uuid

from ..config.engine import Base

class User(Base):
    __tablename__ = 'users'

    id : str = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    username : str = Column(String, unique=True)
    pwd : str = Column(String)
    fullname: str = Column(String)
    birthdate: str= Column(String, nullable=True)
    created_at: str = Column(TIMESTAMP, server_default=func.now()) 
    updated_at: str = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()) 