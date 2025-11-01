from typing import Optional
from uuid import UUID

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from fast_api_template.modules.shared.errors.entity_not_found_error import EntityNotFoundError
from fast_api_template.modules.user.repository.schemas.edit_user_schema import EditUserSchema
from fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from fast_api_template.modules.user.user import User


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

    async def delete(self, user_uuid: UUID) -> None:
        statement = select(User).where(User.uuid == user_uuid)
        result = await self.session.exec(statement)
        user = result.first()
        await self.session.delete(user)
        await self.session.commit()

    async def get_with_email(self, email: str) -> User:
        statement = select(User).where(User.email == email)
        result = await self.session.exec(statement)
        user = result.first()

        if not user:
            raise EntityNotFoundError

        return user

    async def edit(self, user_id: int, partial_user: EditUserSchema) -> User:
        statement = select(User).where(User.id == user_id)
        result = await self.session.exec(statement)
        user = result.first()

        if not user:
            raise EntityNotFoundError

        for key, value in partial_user.model_dump(exclude_unset=True).items():
            setattr(user, key, value)

        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def get_with_stripe_customer_id(self, stripe_customer_id: str) -> User:
        statement = select(User).where(User.stripe_customer_id == stripe_customer_id)
        result = await self.session.exec(statement)
        user = result.first()

        if not user:
            raise EntityNotFoundError

        return user

