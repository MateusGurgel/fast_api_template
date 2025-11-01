from .deactivate_subscription_dto import (
    DeactivateSubscriptionResponseDTO,
    DeactivateSubscriptionDTO,
)
from .deactivate_subscription_injection import (
    InjectDeactivateSubscriptionUseCase,
)
from .deactivate_subscription_use_case import (
    DeactivateSubscriptionUseCase,
)


async def deactivate_subscription_controller(
    dto: DeactivateSubscriptionDTO, deactivate_subscription_use_case: DeactivateSubscriptionUseCase = InjectDeactivateSubscriptionUseCase
) -> DeactivateSubscriptionResponseDTO:
    result = deactivate_subscription_use_case.handle(dto)
    return await result