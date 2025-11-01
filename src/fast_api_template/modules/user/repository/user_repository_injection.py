from fastapi import Depends
from fast_api_template.modules.shared.dependency_injections.postgree_session import (
    PGSession,
)
from fast_api_template.modules.user.repository.user_repository import UserRepository
from sqlmodel.ext.asyncio.session import AsyncSession


def inject_user_repository(session: AsyncSession = PGSession) -> UserRepository:
    return UserRepository(session)


InjectUserRepository = Depends(inject_user_repository)
