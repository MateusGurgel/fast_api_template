from fastapi import APIRouter

from fast_api_template.modules.health_check.infra.health_check_router import (
    health_check_router,
)
from fast_api_template.infra.v1_router import router_v1

router = APIRouter()
router.include_router(router_v1, prefix="/v1")
router.include_router(health_check_router)
