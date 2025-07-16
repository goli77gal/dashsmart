# ---------- app/models/models.py ----------
from sqlalchemy import Column, String, Boolean, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    role = Column(String, default="viewer")
    totp_secret = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class App(Base):
    __tablename__ = "apps"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    store_app_id = Column(String, nullable=False)

class Metadata(Base):
    __tablename__ = "metadata"
    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(Integer, ForeignKey("apps.id"))
    language = Column(String, nullable=False)
    field = Column(String, nullable=False)
    content = Column(Text)
    last_updated_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

class Setting(Base):
    __tablename__ = "settings"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(Text)
    is_secret = Column(Boolean, default=True)