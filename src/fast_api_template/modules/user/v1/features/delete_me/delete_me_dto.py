from fast_api_template.modules.shared.base_dto import BaseDTO
from fast_api_template.modules.user.user import User


class DeleteMeDTO(BaseDTO):
    me: User


class DeleteMeResponseDTO(BaseDTO):
    message: str
