from fast_api_template.modules.shared.base_use_case import BaseUseCase

from .activate_subscription_dto import (
    ActivateSubscriptionDTO,
    ActivateSubscriptionResponseDTO,
)


class ActivateSubscriptionUseCase(BaseUseCase[ActivateSubscriptionDTO, ActivateSubscriptionResponseDTO]):

    def __init__(self) -> None:
        pass

    async def handle(self, dto: ActivateSubscriptionDTO) -> ActivateSubscriptionResponseDTO:
        pass