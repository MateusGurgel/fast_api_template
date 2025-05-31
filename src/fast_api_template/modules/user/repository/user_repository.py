from sqlmodel import Session

from src.fast_api_template.modules.user.repository.schemas.create_user_schema import (
    CreateUserSchema,
)
from src.fast_api_template.modules.user.user import User


class UserRepository:

    def __init__(self, db: Session) -> None:
        self.db: Session = db

    def create(self, create_user_schema: CreateUserSchema) -> User:
        user = User(
            password=create_user_schema.hashed_password, email=create_user_schema.email
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
