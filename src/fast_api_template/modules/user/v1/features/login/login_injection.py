from fastapi import Depends
from fast_api_template.modules.user.repository.user_repository_injection import (
    InjectUserRepository,
)
from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.v1.features.login.login_use_case import (
    LoginUseCase,
)


def get_login_use_case(
    user_repository: UserRepository = InjectUserRepository,
) -> LoginUseCase:
    return LoginUseCase(user_repository)


GetLoginUseCase = Depends(get_login_use_case)
