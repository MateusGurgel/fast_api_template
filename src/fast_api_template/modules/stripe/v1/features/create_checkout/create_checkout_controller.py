from .create_checkout_dto import (
    CreateCheckoutResponseDTO,
    CreateCheckoutDTO,
)
from .create_checkout_injection import (
    InjectCreateCheckoutUseCase,
)
from .create_checkout_use_case import (
    CreateCheckoutUseCase,
)


async def create_checkout_controller(
    dto: CreateCheckoutDTO, create_checkout_use_case: CreateCheckoutUseCase = InjectCreateCheckoutUseCase
) -> CreateCheckoutResponseDTO:
    result = create_checkout_use_case.handle(dto)
    return await result