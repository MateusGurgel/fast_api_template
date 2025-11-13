from typing import Protocol, Optional
from uuid import UUID

from fast_api_template.modules.subscription_plan.repository.schemas.create_subscription_plan_schema import \
    CreateSubscriptionPlanSchema
from fast_api_template.modules.subscription_plan.subscription import SubscriptionPlan
from fast_api_template.modules.user.repository.schemas.edit_user_schema import EditUserSchema
from fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from fast_api_template.modules.user.user import User


class SubscriptionPlanRepositoryContract(Protocol):
    async def create(self, create_subscription_plan_schema: CreateSubscriptionPlanSchema) -> SubscriptionPlan: ...
    async def get_with_uuid(self, uuid: UUID) -> SubscriptionPlan: ...
    async def get_with_stripe_price_id(self, stripe_price_id: str) -> SubscriptionPlan: ...