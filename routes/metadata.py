from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import models
from app.models.schemas import MetadataField
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MetadataField)
def set_metadata(meta: MetadataField, db: Session = Depends(get_db)):
    existing = db.query(models.Metadata).filter(
        models.Metadata.app_id == meta.app_id,
        models.Metadata.language == meta.language,
        models.Metadata.field == meta.field
    ).first()
    if existing:
        existing.content = meta.content
    else:
        new_meta = models.Metadata(**meta.dict())
        db.add(new_meta)
    db.commit()
    return meta

@router.get("/", response_model=List[MetadataField])
def list_metadata(db: Session = Depends(get_db)):
    return db.query(models.Metadata).all()
