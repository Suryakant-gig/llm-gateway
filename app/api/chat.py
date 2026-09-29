from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_api_key
from app.models.api_key import APIKey
from app.models.schemas import ChatRequest
from app.services.router import route_request
from app.services.cost import calculate_cost
from app.services.usage import record_usage


router = APIRouter()

@router.post("/chat")
def chat(
    request: ChatRequest,
    api_key: APIKey = Depends(get_current_api_key),
    db: Session = Depends(get_db),
):
    response = route_request(
        message=request.message,
        model=request.model,
    )

    cost = calculate_cost(
        model=response.model,
        input_tokens=response.input_tokens,
        output_tokens=response.output_tokens,
    )

    record_usage(
        db=db,
        api_key=api_key,
        response=response,
        estimated_cost=cost,
    )

    return response