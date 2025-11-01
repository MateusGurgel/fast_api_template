from typing import Optional

from pydantic import BaseModel


class EditUserSchema(BaseModel):
    hashed_password: Optional[str] = None
    stripe_session_id: Optional[str] = None
