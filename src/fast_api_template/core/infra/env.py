from pydantic import (
    PostgresDsn,
)

from pydantic_settings import BaseSettings


class ENV(BaseSettings):
    postgres_url: PostgresDsn
    salt: str
    pepper: str
    secret: str
    jwt_ttl: int

    base_url: str

    stripe_api_key: str
    stripe_public_key: str
    stripe_webhook_secret: str
    stripe_success_url: str
    stripe_failure_url: str


env = ENV(_env_file=".env", _env_file_encoding="utf-8")
