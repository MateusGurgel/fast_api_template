from fast_api_template.modules.shared.base_use_case import BaseUseCase

from .deactivate_subscription_dto import (
    DeactivateSubscriptionDTO,
    DeactivateSubscriptionResponseDTO,
)


class DeactivateSubscriptionUseCase(BaseUseCase[DeactivateSubscriptionDTO, DeactivateSubscriptionResponseDTO]):

    def __init__(self) -> None:
        pass

    async def handle(self, dto: DeactivateSubscriptionDTO) -> DeactivateSubscriptionResponseDTO:
        pass