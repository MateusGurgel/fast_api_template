from fastapi import APIRouter

from fast_api_template.modules.user.v1.features.create_user.create_user_controller import (
    create_user_controller,
)
from fast_api_template.modules.user.v1.features.delete_me.delete_me_controller import (
    delete_me_controller,
)
from fast_api_template.modules.user.v1.features.get_me.get_me_controller import (
    get_me_controller,
)
from fast_api_template.modules.user.v1.features.login.login_controller import (
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

user_router_v1.add_api_route(
    "/me", get_me_controller, methods=["GET"], description="Get current logged user"
)

user_router_v1.add_api_route(
    "/me",
    delete_me_controller,
    methods=["DELETE"],
    description="Delete user",
)
