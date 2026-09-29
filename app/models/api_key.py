from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.core.database import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)

    team_id = Column(
        Integer,
        ForeignKey("teams.id"),
        nullable=False,
    )

    key_hash = Column(
        String(128),
        unique=True,
        nullable=False,
    )

    is_active = Column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    last_used_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )