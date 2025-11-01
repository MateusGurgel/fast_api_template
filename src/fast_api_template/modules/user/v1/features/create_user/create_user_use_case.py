from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError

from fast_api_template.modules.shared.base_use_case import BaseUseCase
from fast_api_template.modules.shared.utils.crypto import hash_string
from fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from fast_api_template.modules.user.repository.user_repository_contract import (
    UserRepositoryContract,
)
from fast_api_template.modules.user.v1.features.create_user.create_user_dto import (
    CreateUserDTO,
    CreateUserResponseDTO,
)


class CreateUserUseCase(BaseUseCase[CreateUserDTO, CreateUserResponseDTO]):

    def __init__(self, user_repository: UserRepositoryContract):
        self.user_repository = user_repository

    async def handle(self, dto: CreateUserDTO) -> CreateUserResponseDTO:

        hashed_password = hash_string(dto.password)

        try:
            await self.user_repository.create(
                CreateUserSchema(email=dto.email, hashed_password=hashed_password)
            )
        except IntegrityError:
            raise HTTPException(status_code=400, detail="The email already exists")

        return CreateUserResponseDTO(message="Ok")
