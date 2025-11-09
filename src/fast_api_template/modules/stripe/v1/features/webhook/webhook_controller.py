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
from fastapi import Request, HTTPException


async def webhook_controller(
    request: Request, webhook_use_case: WebhookUseCase = InjectWebhookUseCase
) -> WebhookResponseDTO:

    signature = request.headers.get('stripe-signature')

    if not signature:
        raise HTTPException(status_code=400, detail="Missing signature header")

    result = webhook_use_case.handle(WebhookDTO(
        signature=signature,
        body=await request.body(),
    ))
    return await result