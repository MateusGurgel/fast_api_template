from fastapi import Depends
from fast_api_template.modules.shared.dependency_injections.postgree_session import (
    PGSession,
)
from fast_api_template.modules.subscription_plan.repository.subscription_plan_repository import \
    SubscriptionPlanRepository
from fast_api_template.modules.user.repository.user_repository import UserRepository
from sqlmodel.ext.asyncio.session import AsyncSession


def inject_subscription_plan_repository(session: AsyncSession = PGSession) -> SubscriptionPlanRepository:
    return SubscriptionPlanRepository(session)


InjectSubscriptionPlanRepository = Depends(inject_subscription_plan_repository)
