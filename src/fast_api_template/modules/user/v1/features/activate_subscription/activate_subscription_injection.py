from fastapi import Depends

from .activate_subscription_use_case import (
    ActivateSubscriptionUseCase,
)


def inject_activate_subscription_use_case() -> ActivateSubscriptionUseCase:
    return ActivateSubscriptionUseCase()


InjectActivateSubscriptionUseCase = Depends(inject_activate_subscription_use_case)