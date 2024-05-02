import os

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Application"
    DEBUG_MODE: bool = False

    # Database settings
    DATABASE_URL: str = Field(default="sqlite:///./test.db")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


# Environment-specific settings can be added by subclassing
class DevelopmentSettings(Settings):
    DEBUG_MODE: bool = True


class ProductionSettings(Settings):
    DEBUG_MODE: bool = False


# Function to load the correct settings based on an environment variable
def get_settings() -> Settings:
    env = os.getenv("FASTAPI_ENV", "development")
    if env.lower() == "production":
        print("Running in production mode")
        return ProductionSettings()
    print("Running in development mode")
    return DevelopmentSettings()


settings = get_settings()
