from fastapi import Depends

from fast_api_template.core.infra.env import env
from .create_checkout_use_case import (
    CreateCheckoutUseCase,
)


def inject_create_checkout_use_case() -> CreateCheckoutUseCase:
    return CreateCheckoutUseCase(
        stripe_failure_url=env.stripe_failure_url,
        stripe_success_url=env.stripe_success_url,
    )


InjectCreateCheckoutUseCase = Depends(inject_create_checkout_use_case)