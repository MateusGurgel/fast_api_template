import stripe
from envs.venv.Lib.http.client import HTTPException

from src.fast_api_template.modules.shared.base_use_case import BaseUseCase

from .create_checkout_dto import (
    CreateCheckoutDTO,
    CreateCheckoutResponseDTO,
)


class CreateCheckoutUseCase(BaseUseCase[CreateCheckoutDTO, CreateCheckoutResponseDTO]):

    def __init__(self, stripe_success_url: str, stripe_failure_url: str) -> None:
        self.stripe_success_url = stripe_success_url
        self.stripe_failure_url = stripe_failure_url


    async def handle(self, dto: CreateCheckoutDTO) -> CreateCheckoutResponseDTO:

        try:
            prices = stripe.Price.list(
                lookup_keys=[dto.plan],
                expand=['data.product']
            )

            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price': prices.data[0].id,
                        'quantity': 1,
                    },
                ],
                mode='subscription',
                success_url=self.stripe_success_url,
                cancel_url=self.stripe_failure_url,
            )

            return CreateCheckoutResponseDTO(
                checkout_url=checkout_session.url
            )
        except Exception as e:
            raise HTTPException()

