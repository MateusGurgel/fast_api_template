from pydantic import EmailStr

from fast_api_template.modules.shared.base_dto import BaseDTO


class CreateUserDTO(BaseDTO):
    email: EmailStr
    password: str


class CreateUserResponseDTO(BaseDTO):
    message: str
