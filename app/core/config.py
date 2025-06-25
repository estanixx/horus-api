# app/core/config.py
"""
Application Configuration Management.

This module centralizes the application's configuration. It uses python-dotenv
to load environment variables from a `.env` file and provides a single `Settings`
class that reads these variables.

A global `settings` object is instantiated for easy access to configuration
values throughout the project (e.g., `from app.core.config import settings`).
"""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file into the environment.
# This line makes it possible to use a .env file for local development
# without having to manually `export` variables in the shell.
load_dotenv()


class Settings:
    """
    Encapsulates all application settings.

    This class reads configuration values from the environment variables, providing
    sensible default values for local development if a variable is not set.

    Attributes:
        PROJECT_NAME (str): The name of the project.
        DATABASE_URL (str): The connection string for the database.
    """
    def __init__(self):
        """Initializes the Settings instance by reading from environment variables."""
        # Read from environment variables, or use a default value if not set.
        self.PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Horus API")
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", '')

        # You can add more settings here as needed.
        # It's good practice to handle type conversion for non-string values.
        # self.DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
        # self.SECRET_KEY: str = os.getenv("SECRET_KEY", "a-secure-default-secret-key")


# Create a single, global instance of the Settings class.
# This object will be imported by other modules to access configuration values.
settings = Settings()