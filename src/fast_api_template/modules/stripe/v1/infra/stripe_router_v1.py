from fastapi import APIRouter

from fast_api_template.modules.stripe.v1.features.create_checkout.create_checkout_controller import \
    create_checkout_controller
from fast_api_template.modules.stripe.v1.features.webhook.webhook_controller import webhook_controller

stripe_router_v1 = APIRouter(prefix="/stripe", tags=["Stripe"])

stripe_router_v1.add_api_route(
    "/checkout", create_checkout_controller, methods=["POST"], description="Create the user checkout"
)

stripe_router_v1.add_api_route("/webhook", webhook_controller, methods=["POST"], description="Stripe webhook")