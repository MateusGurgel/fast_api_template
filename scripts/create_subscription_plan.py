import asyncio

import stripe
import typer

from fast_api_template.core.infra.postgres import get_session_with_context_manager
from fast_api_template.core.infra.env import env
from fast_api_template.modules.subscription_plan.repository.subscription_plan_repository import \
    SubscriptionPlanRepository
from fast_api_template.modules.subscription_plan.subscription import Interval
from fast_api_template.modules.subscription_plan.v1.features.create_subscription_plan.create_subscription_plan_dto import \
    CreateSubscriptionPlanDTO
from fast_api_template.modules.subscription_plan.v1.features.create_subscription_plan.create_subscription_plan_use_case import \
    CreateSubscriptionPlanUseCase

app = typer.Typer(help="Manages subscriptions")
stripe.api_key = env.stripe_api_key

@app.command()
def run(
        name: str = typer.Argument(..., help="Name to use for the subscription plan"),
        price: int = typer.Argument(..., help="Price in cents to use for the subscription plan"),
        currency: str = typer.Argument("usd", help="Currency to use for the subscription plan"),
        billing_interval: Interval = typer.Argument(Interval.MONTH, help="Interval to use for the subscription plan"),
) -> None:

    async def run_async() -> None:
        async with get_session_with_context_manager() as session:
            subscription_plan_repository: SubscriptionPlanRepository = SubscriptionPlanRepository(session)
            creating_subscription_plan_use_case: CreateSubscriptionPlanUseCase = CreateSubscriptionPlanUseCase(subscription_plan_repository)

            await creating_subscription_plan_use_case.handle(
                CreateSubscriptionPlanDTO(
                    currency=currency,
                    price=price,
                    billing_interval=billing_interval,
                    name=name,
                )
            )



    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_async())



if __name__ == "__main__":
    app()