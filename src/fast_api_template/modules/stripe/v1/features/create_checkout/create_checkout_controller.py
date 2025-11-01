from fast_api_template.modules.shared.dependency_injections.require_user_injection import GetCurrentUser
from fast_api_template.modules.user.user import User
from .create_checkout_dto import (
    CreateCheckoutResponseDTO,
    CreateCheckoutRequestDTO, CreateCheckoutDTO,
)
from .create_checkout_injection import (
    InjectCreateCheckoutUseCase,
)
from .create_checkout_use_case import (
    CreateCheckoutUseCase,
)


async def create_checkout_controller(
    dto: CreateCheckoutRequestDTO,
    user: User = GetCurrentUser,
    create_checkout_use_case: CreateCheckoutUseCase = InjectCreateCheckoutUseCase
) -> CreateCheckoutResponseDTO:

    result = create_checkout_use_case.handle(CreateCheckoutDTO(
        user=user,
        **dto.model_dump(),
    ))

    return await result