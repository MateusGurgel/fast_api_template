from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
import uuid


class BaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    uuid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: Optional[datetime] = Field(
        default_factory=datetime.utcnow, nullable=False
    )
