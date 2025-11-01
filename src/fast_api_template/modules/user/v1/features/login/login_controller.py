from fast_api_template.modules.user.v1.features.login.login_dto import (
    LoginDTO,
    LoginResponseDTO,
)
from fast_api_template.modules.user.v1.features.login.login_injection import (
    GetLoginUseCase,
)
from fast_api_template.modules.user.v1.features.login.login_use_case import (
    LoginUseCase,
)


async def login_controller(
    dto: LoginDTO, login_use_case: LoginUseCase = GetLoginUseCase
) -> LoginResponseDTO:
    return await login_use_case.handle(dto)
