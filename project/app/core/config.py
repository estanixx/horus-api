# app/core/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
# By default, load_dotenv() looks for .env in the current directory
# or parent directories until it finds one.
load_dotenv()

class Settings:
    def __init__(self):
        # Read from environment variables, or use a default value if not set
        self.PROJECT_NAME: str = os.getenv("PROJECT_NAME", "My GraphQL FastAPI Project")
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./database.db")

        # You can add more settings here as needed
        # self.DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
        # self.SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")

settings = Settings()