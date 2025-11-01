from .activate_subscription_dto import (
    ActivateSubscriptionResponseDTO,
    ActivateSubscriptionDTO,
)
from .activate_subscription_injection import (
    InjectActivateSubscriptionUseCase,
)
from .activate_subscription_use_case import (
    ActivateSubscriptionUseCase,
)


async def activate_subscription_controller(
    dto: ActivateSubscriptionDTO, activate_subscription_use_case: ActivateSubscriptionUseCase = InjectActivateSubscriptionUseCase
) -> ActivateSubscriptionResponseDTO:
    result = activate_subscription_use_case.handle(dto)
    return await result