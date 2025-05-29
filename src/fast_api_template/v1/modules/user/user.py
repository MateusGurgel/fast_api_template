from datetime import datetime
from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from typing import Optional
import uuid


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        unique=True,
        index=True,
        nullable=False,
    )
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    pid: str = Field(nullable=False)
    email: EmailStr = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
