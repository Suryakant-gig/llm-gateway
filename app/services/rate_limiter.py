from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.api_key import APIKey


DAILY_REQUEST_LIMIT = 2


def check_rate_limit(db: Session, api_key: APIKey):
    now = datetime.now(timezone.utc)

    # TODO: store/read a real daily request counter.
    # For now this is the interface the API layer will use.

    return True