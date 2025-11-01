from typing import Optional
from uuid import UUID

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from fast_api_template.modules.shared.errors.entity_not_found_error import EntityNotFoundError
from fast_api_template.modules.subscription_plan.repository.schemas.create_subscription_plan_schema import \
    CreateSubscriptionPlanSchema
from fast_api_template.modules.subscription_plan.subscription import SubscriptionPlan
from fast_api_template.modules.user.repository.schemas.edit_user_schema import EditUserSchema
from fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from fast_api_template.modules.user.user import User


class SubscriptionPlanRepository:

    def __init__(self, db: AsyncSession) -> None:
        self.session: AsyncSession = db

    async def create(self, create_subscription_plan_schema: CreateSubscriptionPlanSchema) -> SubscriptionPlan:
        subscription_plan = SubscriptionPlan(
            **create_subscription_plan_schema.model_dump()
        )

        self.session.add(subscription_plan)
        await self.session.commit()
        await self.session.refresh(subscription_plan)
        return subscription_plan
