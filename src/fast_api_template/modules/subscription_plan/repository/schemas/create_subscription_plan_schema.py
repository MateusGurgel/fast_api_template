from typing import Optional

from pydantic import BaseModel

from fast_api_template.modules.subscription_plan.subscription import Interval


class CreateSubscriptionPlanSchema(BaseModel):
    name: str
    price: int
    stripe_price_id: str
    currency: Optional[str] = "usd"
    billing_interval: Optional[Interval] = Interval.MONTH
    description: Optional[str] = None
    interval_count: Optional[int] = None
    trial_period_days: Optional[int] = None
    active: Optional[bool] = None
