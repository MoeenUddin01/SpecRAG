"""Unit tests for src/core module (config and logger)."""

import logging
import pytest
from src.core.config import Settings, get_settings
from src.core.logger import setup_logger


def test_default_settings():
    """Test default configuration loading."""
    settings = Settings()
    assert settings.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]
    assert settings.ENVIRONMENT in ["development", "test", "production"]


def test_custom_settings(monkeypatch):
    """Test settings override from environment variables."""
    monkeypatch.setenv("GROQ_API_KEY", "test_groq_key")
    monkeypatch.setenv("JINA_API_KEY", "test_jina_key")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("ENVIRONMENT", "test")

    settings = Settings()
    assert settings.GROQ_API_KEY == "test_groq_key"
    assert settings.JINA_API_KEY == "test_jina_key"
    assert settings.LOG_LEVEL == "DEBUG"
    assert settings.ENVIRONMENT == "test"


def test_validate_keys_success():
    """Test validate_keys when required environment variables are set."""
    settings = Settings(GROQ_API_KEY="valid_groq", JINA_API_KEY="valid_jina")
    # Should not raise any exception
    settings.validate_keys()


def test_validate_keys_failure():
    """Test validate_keys raises ValueError when API keys are missing."""
    settings = Settings(GROQ_API_KEY=None, JINA_API_KEY=None)
    with pytest.raises(ValueError, match="Missing required environment variables"):
        settings.validate_keys()


def test_get_settings_cached():
    """Test get_settings returns a valid cached Settings instance."""
    s1 = get_settings()
    s2 = get_settings()
    assert s1 is s2


def test_setup_logger():
    """Test setup_logger creates a properly configured logger."""
    test_logger = setup_logger(name="test_logger", level="DEBUG")
    assert test_logger.name == "test_logger"
    assert test_logger.level == logging.DEBUG
    assert len(test_logger.handlers) >= 1
