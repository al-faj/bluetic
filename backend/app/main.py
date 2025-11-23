from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from . import models
from . import auth, websocket_notifications

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student Performance Prediction - Haldia Institute of Technology")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(websocket_notifications.router, prefix="/ws")

@app.get("/health")
async def health():
    return {"status": "ok"}
