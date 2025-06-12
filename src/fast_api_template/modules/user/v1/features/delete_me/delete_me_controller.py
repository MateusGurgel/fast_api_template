from src.fast_api_template.modules.shared.dependency_injections.require_user_injection import (
    GetCurrentUser,
)
from src.fast_api_template.modules.user.user import User
from .delete_me_dto import (
    DeleteMeResponseDTO,
    DeleteMeDTO,
)
from .delete_me_injection import (
    GetDeleteMeUseCase,
)
from .delete_me_use_case import (
    DeleteMeUseCase,
)


async def delete_me_controller(
    delete_me_use_case: DeleteMeUseCase = GetDeleteMeUseCase,
    user: User = GetCurrentUser,
) -> DeleteMeResponseDTO:

    dto: DeleteMeDTO = DeleteMeDTO(
        me=user,
    )
    result = delete_me_use_case.handle(dto)
    return await result
