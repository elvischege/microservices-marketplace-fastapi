import secrets
from pydantic import BaseSettings

# Security
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "IeloroChatAPI"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"


settings = Settings()
