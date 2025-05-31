from src.fast_api_template.modules.user.v1.features.create_user.create_user_dto import (
    CreateUserResponseDTO,
    CreateUserDTO,
)
from src.fast_api_template.modules.user.v1.features.create_user.create_user_injection import (
    GetCreateUserUseCase,
)
from src.fast_api_template.modules.user.v1.features.create_user.create_user_use_case import (
    CreateUserUseCase,
)


async def create_user_controller(
    dto: CreateUserDTO, create_user_use_case: CreateUserUseCase = GetCreateUserUseCase
) -> CreateUserResponseDTO:
    result = create_user_use_case.handle(dto)
    return await result
