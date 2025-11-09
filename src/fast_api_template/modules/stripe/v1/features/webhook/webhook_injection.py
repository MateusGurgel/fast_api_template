from fastapi import Depends

from fast_api_template.core.infra.env import env
from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.repository.user_repository_injection import InjectUserRepository
from .webhook_use_case import (
    WebhookUseCase,
)


def inject_webhook_use_case(user_repository: UserRepository = InjectUserRepository) -> WebhookUseCase:
    return WebhookUseCase(
        stripe_webhook_secret=env.stripe_webhook_secret,
        user_repository=user_repository)


InjectWebhookUseCase = Depends(inject_webhook_use_case)