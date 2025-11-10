from enum import Enum
from typing import Optional

from fast_api_template.modules.shared.base_model import BaseModel
from sqlmodel import Field

class BillingInterval(str, Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    YEAR = "year"

class SubscriptionPlan(BaseModel, table=True):
    __tablename__ = "subscription_plan"

    name: str = Field(nullable=False, unique=True)
    price: int = Field(nullable=False, description="Price in cents")
    stripe_price_id: str = Field(nullable=False)

    description: Optional[str] = Field(nullable=True)
    currency: str = Field(nullable=False, default="usd")
    billing_interval: BillingInterval = Field(nullable=False, default=BillingInterval.MONTH)
    interval_count: int = Field(nullable=False, default=1)
    trial_period_days: int = Field(nullable=False, default=0)
    active: bool = Field(nullable=False, default=True)




