from app.core.database import Base, engine

# Import ALL models before create_all()
from app.models.team import Team
from app.models.api_key import APIKey
from app.models.usage import DailyUsage

print("Registered tables:")
print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

print("All tables created")