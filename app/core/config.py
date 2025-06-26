import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Horus API")
        self.DATABASE_URL: str = os.getenv("DATABASE_URL", '')

settings = Settings()