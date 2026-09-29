from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric
from sqlalchemy.sql import func

from app.core.database import Base


class DailyUsage(Base):
    __tablename__ = "daily_usage"

    id = Column(Integer, primary_key=True)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

    api_key_id = Column(Integer, ForeignKey("api_keys.id"), nullable=False)

    usage_date = Column(Date, nullable=False)

    request_count = Column(Integer, default=0, nullable=False)
    input_tokens = Column(Integer, default=0, nullable=False)
    output_tokens = Column(Integer, default=0, nullable=False)
    total_tokens = Column(Integer, default=0, nullable=False)

    estimated_cost = Column(
        Numeric(12, 8),
        default=0,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )