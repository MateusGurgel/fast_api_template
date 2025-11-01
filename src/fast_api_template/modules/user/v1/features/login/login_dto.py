from datetime import datetime
from typing import Optional

from pydantic import EmailStr

from fast_api_template.modules.shared.base_dto import BaseDTO


class LoginDTO(BaseDTO):
    email: EmailStr
    password: str
    grant_type: Optional[str] = "password"


class LoginResponseDTO(BaseDTO):
    token: str
    expires_at: datetime
