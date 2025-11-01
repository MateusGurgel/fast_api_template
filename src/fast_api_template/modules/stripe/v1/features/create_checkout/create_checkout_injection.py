from fastapi import Depends

from fast_api_template.core.infra.env import env
from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.repository.user_repository_injection import InjectUserRepository
from .create_checkout_use_case import (
    CreateCheckoutUseCase,
)


def inject_create_checkout_use_case(user_repository: UserRepository = InjectUserRepository) -> CreateCheckoutUseCase:
    return CreateCheckoutUseCase(
        user_repository=user_repository,
        stripe_failure_url=env.stripe_failure_url,
        stripe_success_url=env.stripe_success_url,
    )


InjectCreateCheckoutUseCase = Depends(inject_create_checkout_use_case)