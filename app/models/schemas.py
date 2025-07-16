# ---------- app/models/schemas.py ----------
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_active: bool
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class AppCreate(BaseModel):
    name: str
    platform: str
    store_app_id: str

class MetadataField(BaseModel):
    app_id: int
    language: str
    field: str
    content: str

class SettingSchema(BaseModel):
    key: str
    value: str
    is_secret: Optional[bool] = True
