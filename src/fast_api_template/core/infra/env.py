from pydantic import (
    PostgresDsn,
)

from pydantic_settings import BaseSettings


class ENV(BaseSettings):
    postgres_url: PostgresDsn
    salt: str
    pepper: str


env = ENV(_env_file=".env", _env_file_encoding="utf-8")
