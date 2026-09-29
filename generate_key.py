from app.core.database import SessionLocal
from app.models.team import Team
from app.services.api_key_service import create_api_key


db = SessionLocal()

try:
    raw_key = create_api_key(db, team_id=2)
    print("NEW GATEWAY API KEY:")
    print(raw_key)
finally:
    db.close()