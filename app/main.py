from fastapi import FastAPI

# Register all SQLAlchemy models
from app.models.team import Team
from app.models.api_key import APIKey
from app.models.usage import DailyUsage

from app.api.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)