from fastapi import Depends
from fast_api_template.modules.user.repository.user_repository_injection import (
    InjectUserRepository,
)
from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.v1.features.create_user.create_user_use_case import (
    CreateUserUseCase,
)


def get_create_user_use_case(
    user_repository: UserRepository = InjectUserRepository,
) -> CreateUserUseCase:
    return CreateUserUseCase(user_repository)


GetCreateUserUseCase = Depends(get_create_user_use_case)
