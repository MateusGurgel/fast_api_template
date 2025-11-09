import asyncio

from fast_api_template.core.infra.postgres import create_db_and_tables
from fast_api_template.modules.subscription_plan.subscription import SubscriptionPlan

def run() -> None:
    asyncio.run(create_db_and_tables())
