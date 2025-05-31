from fastapi import Depends
from src.fast_api_template.modules.user.repository.schemas.user_repository_injection import (
    GetUserRepository,
)
from src.fast_api_template.modules.user.repository.user_repository import UserRepository
from src.fast_api_template.modules.user.v1.features.create_user.create_user_use_case import (
    CreateUserUseCase,
)


def get_create_user_use_case(
    user_repository: UserRepository = GetUserRepository,
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)


GetCreateUserUseCase = Depends(get_create_user_use_case)
