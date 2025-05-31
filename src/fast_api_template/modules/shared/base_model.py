from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone
from uuid import UUID, uuid4


class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: UUID = Field(
        default_factory=uuid4,
        nullable=False,
    )
    created_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False
    )
