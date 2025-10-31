from fastapi import APIRouter

from fast_api_template.modules.stripe.v1.infra.stripe_router_v1 import stripe_router_v1
from src.fast_api_template.modules.user.v1.infra.user_router_v1 import user_router_v1

router_v1 = APIRouter(tags=["V1"])

router_v1.include_router(user_router_v1)
router_v1.include_router(stripe_router_v1, prefix="/stripe")