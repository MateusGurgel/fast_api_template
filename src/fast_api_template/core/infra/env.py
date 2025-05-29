from pydantic import (
    PostgresDsn,
)

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_URL: PostgresDsn


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")

print(settings.model_dump())
