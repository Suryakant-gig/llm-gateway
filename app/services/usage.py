from datetime import date

from sqlalchemy.orm import Session

from app.models.api_key import APIKey
from app.models.usage import DailyUsage
from app.services.llm import LLMResponse


def record_usage(
    db: Session,
    api_key: APIKey,
    response: LLMResponse,
    estimated_cost: float,
):
    today = date.today()

    usage = (
        db.query(DailyUsage)
        .filter(
            DailyUsage.api_key_id == api_key.id,
            DailyUsage.usage_date == today,
        )
        .first()
    )

    if usage is None:
        usage = DailyUsage(
            team_id=api_key.team_id,
            api_key_id=api_key.id,
            usage_date=today,
            request_count=0,
            input_tokens=0,
            output_tokens=0,
            total_tokens=0,
            estimated_cost=0,
        )

        db.add(usage)

    usage.request_count += 1
    usage.input_tokens += response.input_tokens
    usage.output_tokens += response.output_tokens
    usage.total_tokens += response.total_tokens
    usage.estimated_cost += estimated_cost

    db.commit()
    db.refresh(usage)

    return usage