from datetime import datetime, timezone
from typing import Optional
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from fast_api_template.modules.shared.errors.entity_not_found_error import EntityNotFoundError
from fast_api_template.modules.shared.utils.crypto import decrypt_jwt
from fast_api_template.modules.user.repository.user_repository import UserRepository
from fast_api_template.modules.user.repository.user_repository_injection import (
    InjectUserRepository,
)
from fast_api_template.modules.user.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/users/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_repository: UserRepository = InjectUserRepository,
) -> User:
    try:
        payload = decrypt_jwt(token)

        if payload.get("email") is None or payload.get("expires_at") is None:
            raise HTTPException(status_code=401, detail="Bad Credentials")

        now: datetime = datetime.now(timezone.utc)
        expires_at: datetime = datetime.fromisoformat(payload["expires_at"])

        if now > expires_at:
            raise HTTPException(status_code=401, detail="Expired Token")

        try:
            user: User = await user_repository.get_with_email(payload["email"])
        except EntityNotFoundError:
            raise HTTPException(status_code=401, detail="Bad Credentials")

        return user
    except jwt.PyJWTError as e:
        print(e)
        raise HTTPException(status_code=401, detail="Token inválido")


GetCurrentUser = Depends(get_current_user)
