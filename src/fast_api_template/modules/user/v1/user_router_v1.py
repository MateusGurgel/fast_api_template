from fastapi import APIRouter

from src.fast_api_template.modules.user.v1.features.create_user.create_user_controller import (
    create_user,
)

user_router_v1 = APIRouter()

user_router_v1.add_api_route(
    "/users", create_user, methods=["POST"], description="Create a User"
)
