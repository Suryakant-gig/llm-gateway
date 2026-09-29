import hashlib

from fastapi import Header, HTTPException, Depends


from app.core.database import SessionLocal
from app.models.api_key import APIKey
from app.core.database import get_db
from sqlalchemy.orm import Session

def hash_api_key(raw_key: str) -> str:
    return hashlib.sha256(raw_key.encode()).hexdigest()


def authenticate_api_key(
    raw_key: str,
    db: Session,
) -> APIKey:

    key_hash = hash_api_key(raw_key)

    api_key = (
        db.query(APIKey)
        .filter(APIKey.key_hash == key_hash)
        .first()
    )

    if api_key is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key",
        )

    if not api_key.is_active:
        raise HTTPException(
            status_code=401,
            detail="API key is inactive",
        )

    return api_key

def get_current_api_key(
    x_api_key: str = Header(...),
    db: Session = Depends(get_db),
) -> APIKey:
    return authenticate_api_key(x_api_key, db)