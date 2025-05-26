from fastapi import APIRouter

from src.fast_api_template.modules.health_check.infra.health_check_router import health_check_router
from src.fast_api_template.v1.infra.v1_router import v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")
router.include_router(health_check_router)