from typing import Protocol, Optional
from src.fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from src.fast_api_template.modules.user.user import User


class UserRepositoryContract(Protocol):
    def create(self, create_user_schema: CreateUserSchema) -> User: ...
    def get_with_email(self, email: str) -> Optional[User]: ...
