from pydantic import (
    PostgresDsn,
)

from pydantic_settings import BaseSettings


class ENV(BaseSettings):
    POSTGRES_URL: PostgresDsn


env = ENV(_env_file=".env", _env_file_encoding="utf-8")
