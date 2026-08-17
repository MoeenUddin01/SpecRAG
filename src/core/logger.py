"""Logging configuration module for SpecRAG."""

import logging
import sys
from typing import Optional


def setup_logger(
    name: str = "specrag",
    level: Optional[str] = None,
    log_format: Optional[str] = None,
) -> logging.Logger:
    """Configures and returns a logger instance.

    Args:
        name: Name of the logger.
        level: Logging level (DEBUG, INFO, WARNING, ERROR). If None, defaults to INFO.
        log_format: Custom log format string.

    Returns:
        Configured logging.Logger instance.
    """
    if level is None:
        level = "INFO"

    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger = logging.getLogger(name)
    logger.setLevel(numeric_level)

    # Avoid adding duplicate handlers if logger is already configured
    if not logger.handlers:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(numeric_level)

        if log_format is None:
            log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        formatter = logging.Formatter(log_format, datefmt="%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


# Default application logger instance
logger = setup_logger()
