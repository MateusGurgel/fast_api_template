from fastapi import APIRouter

from src.fast_api_template.modules.user.v1.features.create_user.create_user_controller import (
    create_user_controller,
)
from src.fast_api_template.modules.user.v1.features.login.login_controller import (
    login_controller,
)

user_router_v1 = APIRouter(prefix="/users", tags=["User"])

user_router_v1.add_api_route(
    "/",
    create_user_controller,
    methods=["POST"],
    description="Create a User",
    status_code=201,
)

user_router_v1.add_api_route(
    "/login", login_controller, methods=["POST"], description="User login"
)
