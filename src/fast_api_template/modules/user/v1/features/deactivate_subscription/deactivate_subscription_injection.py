from fastapi import Depends

from .deactivate_subscription_use_case import (
    DeactivateSubscriptionUseCase,
)


def inject_deactivate_subscription_use_case() -> DeactivateSubscriptionUseCase:
    return DeactivateSubscriptionUseCase()


InjectDeactivateSubscriptionUseCase = Depends(inject_deactivate_subscription_use_case)