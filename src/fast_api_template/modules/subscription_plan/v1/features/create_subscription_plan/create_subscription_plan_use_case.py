import stripe

from fast_api_template.modules.shared.base_use_case import BaseUseCase
from fast_api_template.modules.subscription_plan.repository.schemas.create_subscription_plan_schema import \
    CreateSubscriptionPlanSchema
from fast_api_template.modules.subscription_plan.repository.subscription_plan_repository_contract import \
    SubscriptionPlanRepositoryContract

from .create_subscription_plan_dto import (
    CreateSubscriptionPlanDTO,
    CreateSubscriptionPlanResponseDTO,
)


class CreateSubscriptionPlanUseCase(BaseUseCase[CreateSubscriptionPlanDTO, CreateSubscriptionPlanResponseDTO]):

    def __init__(self, subscription_plan_repository: SubscriptionPlanRepositoryContract) -> None:
        self.subscription_plan_repository: SubscriptionPlanRepositoryContract = subscription_plan_repository

    async def handle(self, dto: CreateSubscriptionPlanDTO) -> CreateSubscriptionPlanResponseDTO:

        new_price = stripe.Price.create(
            currency=dto.currency,
            unit_amount=dto.price,
            recurring={"interval": dto.interval.value},
            product_data={"name": dto.name},
        )

        await self.subscription_plan_repository.create(
            CreateSubscriptionPlanSchema(
                **dto.model_dump(),
                stripe_price_id=new_price.id
            ),
        )

        return CreateSubscriptionPlanResponseDTO(
            message="Subscription Plan created successfully"
        )
