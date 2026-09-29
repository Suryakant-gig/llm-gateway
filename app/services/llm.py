from dataclasses import dataclass

from groq import Groq
from google import genai

from app.core.config import settings


@dataclass
class LLMResponse:
    text: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    total_tokens: int


groq_client = Groq(api_key=settings.groq_api_key)
gemini_client = genai.Client(api_key=settings.gemini_api_key)


def call_groq(message: str) -> LLMResponse:
    response = groq_client.chat.completions.create(
        model=settings.groq_model,
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    usage = response.usage

    return LLMResponse(
        text=response.choices[0].message.content,
        provider="groq",
        model=settings.groq_model,
        input_tokens=usage.prompt_tokens,
        output_tokens=usage.completion_tokens,
        total_tokens=usage.total_tokens,
    )


def call_gemini(message: str) -> LLMResponse:
    response = gemini_client.models.generate_content(
        model=settings.gemini_model,
        contents=message,
    )

    # Token usage can depend on the response/model configuration.
    usage = getattr(response, "usage_metadata", None)

    input_tokens = getattr(usage, "prompt_token_count", 0) if usage else 0
    output_tokens = getattr(usage, "candidates_token_count", 0) if usage else 0
    total_tokens = getattr(usage, "total_token_count", 0) if usage else 0

    return LLMResponse(
        text=response.text,
        provider="gemini",
        model=settings.gemini_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
    )