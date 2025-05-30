from src.fast_api_template.modules.shared.base_use_case import BaseUseCase
from src.fast_api_template.modules.user.v1.use_cases.create_user_use_case.create_user_dto import (
    CreateUserDTO,
    CreateUserResponseDTO,
)


class CreateUserUseCase(BaseUseCase[CreateUserDTO, CreateUserResponseDTO]):

    async def handle(self, dto: CreateUserDTO) -> CreateUserResponseDTO:
        return CreateUserResponseDTO(message="Ok")
