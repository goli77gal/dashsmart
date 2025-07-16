# ---------- app/main.py ----------
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes import auth, settings, users, apps, metadata, translate

load_dotenv()

app = FastAPI(title="Smart Metadata Dashboard")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(settings.router, prefix="/settings", tags=["settings"])
app.include_router(apps.router, prefix="/apps", tags=["apps"])
app.include_router(metadata.router, prefix="/metadata", tags=["metadata"])
app.include_router(translate.router, prefix="/translate", tags=["translate"])

@app.get("/")
def read_root():
    return {"message": "Smart Metadata Dashboard is running"}