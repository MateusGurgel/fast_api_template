from fastapi import Depends
from src.fast_api_template.modules.shared.dependency_injections.postgree_session import (
    PGSession,
)
from src.fast_api_template.modules.user.repository.user_repository import UserRepository
from sqlmodel.ext.asyncio.session import AsyncSession


def get_user_repository(session: AsyncSession = PGSession) -> UserRepository:
    return UserRepository(session)


GetUserRepository = Depends(get_user_repository)
