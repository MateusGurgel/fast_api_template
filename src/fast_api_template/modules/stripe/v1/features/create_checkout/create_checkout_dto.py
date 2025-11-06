import uuid

from fast_api_template.modules.user.user import User
from fast_api_template.modules.shared.base_dto import BaseDTO

class CreateCheckoutRequestDTO(BaseDTO):
    plan_uuid: uuid.UUID


class CreateCheckoutDTO(CreateCheckoutRequestDTO):
    user: User


class CreateCheckoutResponseDTO(BaseDTO):
    checkout_url: str