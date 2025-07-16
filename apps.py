from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models import models
from app.models.schemas import AppCreate
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AppCreate)
def create_app(app: AppCreate, db: Session = Depends(get_db)):
    db_app = models.App(**app.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return app

@router.get("/", response_model=List[AppCreate])
def list_apps(db: Session = Depends(get_db)):
    return db.query(models.App).all()
