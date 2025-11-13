from typing import Dict, Any

import stripe
from fastapi import HTTPException

from fast_api_template.modules.shared.base_use_case import BaseUseCase
from fast_api_template.modules.subscription_plan.repository.subscription_plan_repository_contract import \
    SubscriptionPlanRepositoryContract
from fast_api_template.modules.subscription_plan.subscription import SubscriptionPlan
from fast_api_template.modules.user.repository.user_repository_contract import UserRepositoryContract
from fast_api_template.modules.user.user import User

from .webhook_dto import (
    WebhookDTO,
    WebhookResponseDTO,
)


class WebhookUseCase(BaseUseCase[WebhookDTO, WebhookResponseDTO]):

    def __init__(self, stripe_webhook_secret: str, user_repository: UserRepositoryContract,
                 subscription_plan_repository: SubscriptionPlanRepositoryContract) -> None:
        self.stripe_webhook_secret : str = stripe_webhook_secret
        self.user_repository: UserRepositoryContract = user_repository
        self.subscription_plan_repository: SubscriptionPlanRepositoryContract = subscription_plan_repository

    async def process_payment_failed(self, data: Dict[str | int, Any]) -> None:
        customer_id = data['object']['customer']
        user: User = await self.user_repository.get_with_stripe_customer_id(customer_id)
        await self.user_repository.set_user_subscription_plan(user.id, None)

    async def process_payment_succeeded(self, data: Dict[str | int, Any]) -> None:
        customer_id = data['object']['customer']
        user: User = await self.user_repository.get_with_stripe_customer_id(customer_id)
        stripe_price_id = data['object']['lines']['data'][0]['price']['id']
        plan: SubscriptionPlan = await self.subscription_plan_repository.get_with_stripe_price_id(stripe_price_id)
        await self.user_repository.set_user_subscription_plan(user.id, plan.id)


    async def handle(self, dto: WebhookDTO) -> WebhookResponseDTO:
        signature = dto.signature

        try:
            event = stripe.Webhook.construct_event(  # type: ignore
                payload=dto.body, sig_header=signature, secret=self.stripe_webhook_secret)

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        data = event['data']
        event_type = event["type"]

        if event_type == "invoice.payment_succeeded":
            await self.process_payment_succeeded(data)
        elif event_type == "customer.subscription.deleted":
            await self.process_payment_failed(data)


        return WebhookResponseDTO(status="success")