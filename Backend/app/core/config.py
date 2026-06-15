from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "changeme"
    UPLOAD_DIR: Path = Path("/tmp/uploads")
    CORS_ORIGINS: list[str] = ["http://localhost:4200", "http://127.0.0.1:4200", "http://localhost:34207"]
    GOOGLE_CLIENT_ID: str | None = None
    JWT_SECRET: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
