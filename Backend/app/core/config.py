import json
from pathlib import Path
from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "changeme"
    UPLOAD_DIR: Path = Path("/tmp/uploads")
    CORS_ORIGINS: list[str] = ["http://localhost:4200", "http://127.0.0.1:4200", "http://localhost:34207"]
    GOOGLE_CLIENT_ID: str | None = None
    JWT_SECRET: str | None = None

    @field_validator("CORS_ORIGINS", mode="before")
    @classmethod
    def parse_cors_origins(cls, value):
        if value is None or value == "":
            return []
        if isinstance(value, str):
            value = value.strip()
            if value.startswith("[") and value.endswith("]"):
                try:
                    decoded = json.loads(value)
                    return [str(item) for item in decoded]
                except ValueError:
                    pass
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
