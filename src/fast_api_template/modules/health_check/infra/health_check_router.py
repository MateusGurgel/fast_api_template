from fastapi import APIRouter

from src.fast_api_template.modules.health_check.use_cases.health_check.health_check_controller import (
    get_api_status,
)

health_check_router = APIRouter()

health_check_router.add_api_route(
    "/", get_api_status, methods=["GET"], description="Api Health Check"
)
