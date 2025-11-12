from typing import Optional

from pydantic import BaseModel


class EditUserSchema(BaseModel):
    hashed_password: Optional[str] = None
    stripe_id: Optional[str] = None
    subscription_plan_id: Optional[int] = None