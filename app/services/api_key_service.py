import hashlib
import secrets

from sqlalchemy.orm import Session

from app.models.api_key import APIKey


def generate_api_key() -> tuple[str, str]:
    raw_key = "gw_" + secrets.token_urlsafe(32)

    key_hash = hashlib.sha256(
        raw_key.encode()
    ).hexdigest()

    return raw_key, key_hash


def create_api_key(db: Session, team_id: int) -> str:
    raw_key, key_hash = generate_api_key()

    api_key = APIKey(
        team_id=team_id,
        key_hash=key_hash,
        is_active=True,
    )

    db.add(api_key)
    db.commit()
    db.refresh(api_key)

    return raw_key