from typing import Literal

from src.fast_api_template.modules.shared.base_dto import BaseDTO


class CreateCheckoutDTO(BaseDTO):
    plan: Literal["Standard"]

class CreateCheckoutResponseDTO(BaseDTO):
    checkout_url: str