from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "LLM Gateway"
    environment: str = "development"

    # Model routing
    default_model: str = "auto"

    database_url: str

    # Gateway limits
    rate_limit_per_minute: int = 2
    monthly_token_quota: int = 5000

    # LLM Providers
    groq_api_key: str | None = None
    gemini_api_key: str | None = None

    # Default models
    groq_model: str = "openai/gpt-oss-20b"
    gemini_model: str = "gemini-3.5-flash-lite"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()