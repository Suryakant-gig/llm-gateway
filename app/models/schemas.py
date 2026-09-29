from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    model: str = "auto"


class Usage(BaseModel):
    input_tokens: int
    output_tokens: int


class ChatResponse(BaseModel):
    response: str
    model: str
    team: str
    usage: Usage