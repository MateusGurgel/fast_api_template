import stripe
from fastapi import HTTPException
from sqlalchemy.testing.suite.test_reflection import metadata
from stripe import Customer

from fast_api_template.modules.shared.base_use_case import BaseUseCase
from fast_api_template.modules.subscription_plan.repository.subscription_plan_repository_contract import \
    SubscriptionPlanRepositoryContract
from fast_api_template.modules.subscription_plan.subscription import SubscriptionPlan
from fast_api_template.modules.user.repository.schemas.edit_user_schema import EditUserSchema
from fast_api_template.modules.user.repository.user_repository_contract import UserRepositoryContract

from .create_checkout_dto import (
    CreateCheckoutDTO,
    CreateCheckoutResponseDTO,
)


class CreateCheckoutUseCase(BaseUseCase[CreateCheckoutDTO, CreateCheckoutResponseDTO]):

    def __init__(self,
                 user_repository: UserRepositoryContract,
                 subscription_plan_repository: SubscriptionPlanRepositoryContract,
                 stripe_success_url: str,
                 stripe_failure_url: str) -> None:
        self.user_repository: UserRepositoryContract = user_repository
        self.stripe_success_url: str = stripe_success_url
        self.stripe_failure_url: str = stripe_failure_url
        self.subscription_plan_repository: SubscriptionPlanRepositoryContract = subscription_plan_repository


    async def handle(self, dto: CreateCheckoutDTO) -> CreateCheckoutResponseDTO:

        try:

            costumer_id: str = dto.user.stripe_session_id

            if not costumer_id:

                new_customer = stripe.Customer.create(
                    email=dto.user.email,
                    metadata={
                        "userId": dto.user.id,
                    }
                )

                await self.user_repository.edit(
                    dto.user.id,
                    EditUserSchema(
                        stripe_session_id=new_customer.id
                    )
                )

                costumer_id = new_customer.id

            plan: SubscriptionPlan = await self.subscription_plan_repository.get_with_uuid(dto.plan_id)

            checkout_session = stripe.checkout.Session.create(
                customer=costumer_id,
                line_items=[
                    {
                        'price': plan.stripe_price_id,
                        'quantity': 1,
                    },
                ],
                metadata={
                    "plan_id": plan.id
                },
                mode='subscription',
                success_url=self.stripe_success_url,
                cancel_url=self.stripe_failure_url,
            )

            if not isinstance(checkout_session.customer, Customer):
                raise Exception("Customer was not created")

            return CreateCheckoutResponseDTO(
                checkout_url=checkout_session.url
            )

        except Exception as e:
            raise HTTPException(500, "Error while creating checkout session, try again later")

