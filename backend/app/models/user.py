"""
USER MODEL 정보
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.db.base import Base

class UserModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(length=100), index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=100), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)