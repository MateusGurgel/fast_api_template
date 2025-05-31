from src.fast_api_template.modules.shared.base_use_case import BaseUseCase
from src.fast_api_template.modules.shared.utils.crypto import hash_string
from src.fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from src.fast_api_template.modules.user.repository.user_repository_contract import (
    UserRepositoryContract,
)
from src.fast_api_template.modules.user.v1.features.create_user.create_user_dto import (
    CreateUserDTO,
    CreateUserResponseDTO,
)


class CreateUserUseCase(BaseUseCase[CreateUserDTO, CreateUserResponseDTO]):

    def __init__(self, user_repository: UserRepositoryContract):
        self.user_repository = user_repository

    async def handle(self, dto: CreateUserDTO) -> CreateUserResponseDTO:

        hashed_password = hash_string(dto.password)

        print(hashed_password)

        self.user_repository.create(
            CreateUserSchema(email=dto.email, hashed_password=hashed_password)
        )

        return CreateUserResponseDTO(message="Ok")
