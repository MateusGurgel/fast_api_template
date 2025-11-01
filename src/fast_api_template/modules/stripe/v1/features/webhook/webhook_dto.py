from typing import Literal

from fast_api_template.modules.shared.base_dto import BaseDTO

class WebhookDTO(BaseDTO):
    signature: str
    body: bytes

class WebhookResponseDTO(BaseDTO):
    status: Literal["success"]