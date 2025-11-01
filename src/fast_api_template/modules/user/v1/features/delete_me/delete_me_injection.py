from fastapi import Depends

from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.repository.user_repository_injection import (
    InjectUserRepository,
)
from .delete_me_use_case import (
    DeleteMeUseCase,
)


def get_delete_me_use_case(
    user_repository: UserRepository = InjectUserRepository,
) -> DeleteMeUseCase:
    return DeleteMeUseCase(user_repository)


GetDeleteMeUseCase = Depends(get_delete_me_use_case)
