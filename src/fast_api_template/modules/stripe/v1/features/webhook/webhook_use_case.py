import stripe
from fastapi import HTTPException

from fast_api_template.modules.shared.base_use_case import BaseUseCase
from fast_api_template.modules.user.repository.user_repository_contract import UserRepositoryContract
from fast_api_template.modules.user.user import User

from .webhook_dto import (
    WebhookDTO,
    WebhookResponseDTO,
)


class WebhookUseCase(BaseUseCase[WebhookDTO, WebhookResponseDTO]):

    def __init__(self, stripe_webhook_secret: str, user_repository: UserRepositoryContract) -> None:
        self.stripe_webhook_secret : str = stripe_webhook_secret
        self.user_repository: UserRepositoryContract = user_repository


    async def handle(self, dto: WebhookDTO) -> WebhookResponseDTO:
        signature = dto.signature

        try:
            event = stripe.Webhook.construct_event(  # type: ignore
                payload=dto.body, sig_header=signature, secret=self.stripe_webhook_secret)

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        data = event['data']
        event_type = event["type"]

        if event_type == "checkout.session.completed":
            customer_id = data['object']['customer']
            user: User = await self.user_repository.get_with_stripe_customer_id(customer_id)
            await self.user_repository.set_user_subscription_plan(user.id, data['object']['metadata']['plan_id'])

        elif event_type == "customer.subscription.deleted":
            customer_id = data['object']['customer']
            user: User = await self.user_repository.get_with_stripe_customer_id(customer_id)
            await self.user_repository.set_user_subscription_plan(user.id, None)


        return WebhookResponseDTO(status="success")