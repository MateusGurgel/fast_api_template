from typing import Protocol, Optional
from uuid import UUID

from src.fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from src.fast_api_template.modules.user.user import User


class UserRepositoryContract(Protocol):
    async def create(self, create_user_schema: CreateUserSchema) -> User: ...
    async def get_with_email(self, email: str) -> Optional[User]: ...
    async def delete(self, user_pid: UUID) -> None: ...
