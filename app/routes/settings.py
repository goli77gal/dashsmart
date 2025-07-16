from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import models
from app.models.schemas import SettingSchema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SettingSchema)
def set_setting(setting: SettingSchema, db: Session = Depends(get_db)):
    existing = db.query(models.Setting).filter(models.Setting.key == setting.key).first()
    if existing:
        existing.value = setting.value
        existing.is_secret = setting.is_secret
    else:
        db.add(models.Setting(**setting.dict()))
    db.commit()
    return setting

@router.get("/", response_model=List[SettingSchema])
def get_all_settings(db: Session = Depends(get_db)):
    return db.query(models.Setting).all()

@router.get("/{key}", response_model=SettingSchema)
def get_setting(key: str, db: Session = Depends(get_db)):
    setting = db.query(models.Setting).filter(models.Setting.key == key).first()
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")
    return setting
