from .webhook_dto import (
    WebhookResponseDTO,
    WebhookDTO,
)
from .webhook_injection import (
    InjectWebhookUseCase,
)
from .webhook_use_case import (
    WebhookUseCase,
)
from fastapi import Request

async def webhook_controller(
    request: Request, webhook_use_case: WebhookUseCase = InjectWebhookUseCase
) -> WebhookResponseDTO:
    result = webhook_use_case.handle(WebhookDTO(
        signature=request.headers.get('stripe-signature'),
        body=await request.body(),
    ))
    return await result