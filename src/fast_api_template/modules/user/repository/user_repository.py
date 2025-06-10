from typing import Optional

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from src.fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from src.fast_api_template.modules.user.user import User


class UserRepository:

    def __init__(self, db: AsyncSession) -> None:
        self.session: AsyncSession = db

    async def create(self, create_user_schema: CreateUserSchema) -> User:
        user = User(
            password=create_user_schema.hashed_password, email=create_user_schema.email
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_with_email(self, email: str) -> Optional[User]:
        statement = select(User).where(User.email == email)
        result = await self.session.exec(statement)
        return result.first()
