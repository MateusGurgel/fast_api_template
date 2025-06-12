from src.fast_api_template.modules.shared.base_use_case import BaseUseCase
from src.fast_api_template.modules.user.repository.user_repository_contract import (
    UserRepositoryContract,
)

from .delete_me_dto import (
    DeleteMeDTO,
    DeleteMeResponseDTO,
)


class DeleteMeUseCase(BaseUseCase[DeleteMeDTO, DeleteMeResponseDTO]):

    def __init__(self, user_repository: UserRepositoryContract):
        self.user_repository = user_repository

    async def handle(self, user_pid: DeleteMeDTO) -> DeleteMeResponseDTO:
        await self.user_repository.delete(user_pid.me.uuid)
        return DeleteMeResponseDTO(message="Ok")
