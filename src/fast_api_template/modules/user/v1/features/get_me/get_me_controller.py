from fast_api_template.modules.shared.dependency_injections.require_user_injection import (
    GetCurrentUser,
)
from fast_api_template.modules.user.user import User
from fast_api_template.modules.user.v1.features.get_me.get_me_dto import (
    GetMeResponseDTO,
)


async def get_me_controller(user: User = GetCurrentUser) -> GetMeResponseDTO:
    response = GetMeResponseDTO(
        email=user.email,
        created_at=user.created_at,
        uuid=user.uuid,
    )
    return response
