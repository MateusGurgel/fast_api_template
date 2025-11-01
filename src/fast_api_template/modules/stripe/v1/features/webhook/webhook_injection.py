from fastapi import Depends

from fast_api_template.core.infra.env import env
from .webhook_use_case import (
    WebhookUseCase,
)


def inject_webhook_use_case() -> WebhookUseCase:
    return WebhookUseCase(env.stripe_webhook_secret)


InjectWebhookUseCase = Depends(inject_webhook_use_case)