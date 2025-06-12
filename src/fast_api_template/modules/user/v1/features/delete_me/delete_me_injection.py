from fastapi import Depends

from src.fast_api_template.modules.user.repository.user_repository import UserRepository
from src.fast_api_template.modules.user.repository.user_repository_injection import (
    GetUserRepository,
)
from .delete_me_use_case import (
    DeleteMeUseCase,
)


def get_delete_me_use_case(
    user_repository: UserRepository = GetUserRepository,
) -> DeleteMeUseCase:
    return DeleteMeUseCase(user_repository)


GetDeleteMeUseCase = Depends(get_delete_me_use_case)
