from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from src.fast_api_template.modules.shared.base_dto import BaseDTO


class GetMeResponseDTO(BaseDTO):
    email: EmailStr
    created_at: datetime
    uuid: UUID
