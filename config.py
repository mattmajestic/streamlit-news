# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    NEWS_API_KEY: str

    class Config:
        env_file = ".env"

# Create an instance of the Settings class
settings = Settings()
