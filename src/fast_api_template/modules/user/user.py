from sqlmodel import Field
from pydantic import EmailStr

from fast_api_template.modules.shared.base_model import BaseModel


class User(BaseModel, table=True):
    email: EmailStr = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
    stripe_session_id: str = Field(nullable=True)
