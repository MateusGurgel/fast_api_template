from datetime import datetime

from pydantic import EmailStr

from src.fast_api_template.modules.shared.base_dto import BaseDTO


class LoginDTO(BaseDTO):
    email: EmailStr
    password: str


class LoginResponseDTO(BaseDTO):
    token: str
    expires_at: datetime
