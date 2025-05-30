from src.fast_api_template.modules.user.v1.use_cases.create_user_use_case.create_user_dto import (
    CreateUserResponseDTO,
    CreateUserDTO,
)
from src.fast_api_template.modules.user.v1.use_cases.create_user_use_case.create_user_use_case import (
    CreateUserUseCase,
)


async def create_user(dto: CreateUserDTO) -> CreateUserResponseDTO:
    create_user_use_case: CreateUserUseCase = CreateUserUseCase()
    result = create_user_use_case.handle(dto)
    return await result
