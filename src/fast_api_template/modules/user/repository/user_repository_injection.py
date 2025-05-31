from fastapi import Depends
from sqlmodel import Session

from src.fast_api_template.modules.shared.dependency_injections.postgree_session import (
    PGSession,
)
from src.fast_api_template.modules.user.repository.user_repository import UserRepository


def get_user_repository(session: Session = PGSession) -> UserRepository:
    return UserRepository(session)


GetUserRepository = Depends(get_user_repository)
