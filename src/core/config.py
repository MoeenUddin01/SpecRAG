"""Configuration management module for SpecRAG."""

import os
from functools import lru_cache
from typing import Optional
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file if available
load_dotenv()


class Settings(BaseSettings):
    """Application settings and environment configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
    )

    # API Keys
    GROQ_API_KEY: Optional[str] = Field(default=None, description="Groq API key for LLM inference")
    JINA_API_KEY: Optional[str] = Field(default=None, description="Jina AI API key for embeddings")

    # Logging & Environment
    LOG_LEVEL: str = Field(default="INFO", description="Logging level (DEBUG, INFO, WARNING, ERROR)")
    ENVIRONMENT: str = Field(default="development", description="Execution environment (development, test, production)")

    def validate_keys(self) -> None:
        """Validate that essential API keys are present for production operations."""
        missing = []
        if not self.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")
        if not self.JINA_API_KEY:
            missing.append("JINA_API_KEY")
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")


@lru_cache()
def get_settings() -> Settings:
    """Return cached instance of Settings."""
    return Settings()


# Default singleton instance
settings = get_settings()
