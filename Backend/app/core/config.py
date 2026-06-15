import json
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_KEY: str = "changeme"
    UPLOAD_DIR: Path = Path("/tmp/uploads")
    CORS_ORIGINS: str | None = Field(default=None, env="CORS_ORIGINS")
    GOOGLE_CLIENT_ID: str | None = None
    JWT_SECRET: str | None = None

    @property
    def cors_origins(self) -> list[str]:
        raw = self.CORS_ORIGINS
        if not raw:
            return ["http://localhost:4200", "http://127.0.0.1:4200", "http://localhost:34207"]
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            try:
                decoded = json.loads(raw)
                return [str(item) for item in decoded]
            except ValueError:
                pass
        return [item.strip() for item in raw.split(",") if item.strip()]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
