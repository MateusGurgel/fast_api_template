import datetime
import hmac
from typing import Optional

from fastapi import HTTPException

from src.fast_api_template.core.infra.env import env
from src.fast_api_template.modules.shared.base_use_case import BaseUseCase
from src.fast_api_template.modules.shared.utils.crypto import (
    hash_string,
    encrypt_payload,
)

from src.fast_api_template.modules.user.repository.user_repository_contract import (
    UserRepositoryContract,
)
from src.fast_api_template.modules.user.user import User
from src.fast_api_template.modules.user.v1.features.login.login_dto import (
    LoginResponseDTO,
    LoginDTO,
)


class LoginUseCase(BaseUseCase[LoginDTO, LoginResponseDTO]):

    def __init__(self, user_repository: UserRepositoryContract):
        self.user_repository = user_repository

    async def handle(self, dto: LoginDTO) -> LoginResponseDTO:

        user: Optional[User] = await self.user_repository.get_with_email(str(dto.email))

        if not user:
            raise HTTPException(status_code=404, detail="Bad Credentials")

        hashed_password = hash_string(dto.password)

        if not hmac.compare_digest(user.password, hashed_password):
            raise HTTPException(status_code=404, detail="Bad Credentials")

        now = datetime.datetime.now(datetime.timezone.utc)
        expires_at = now + datetime.timedelta(seconds=env.jwt_ttl)

        payload = {"email": str(user.email), "expires_at": expires_at.isoformat()}

        token = encrypt_payload(payload)

        return LoginResponseDTO(token=token, expires_at=expires_at)
