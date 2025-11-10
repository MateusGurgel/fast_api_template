from typing import Optional

from fast_api_template.modules.shared.base_dto import BaseDTO
from fast_api_template.modules.subscription_plan.subscription import BillingInterval


class CreateSubscriptionPlanDTO(BaseDTO):
    name: str
    price: int
    currency: str = "usd"
    billing_interval: BillingInterval = BillingInterval.MONTH
    description: Optional[str] = None
    interval_count: Optional[int] = None
    trial_period_days: Optional[int] = None

class CreateSubscriptionPlanResponseDTO(BaseDTO):
    message: str