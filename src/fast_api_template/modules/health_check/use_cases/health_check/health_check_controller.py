from src.fast_api_template.modules.health_check.use_cases.health_check.health_check_dto import HealthCheckResponse

def get_api_status() -> HealthCheckResponse:
    response = HealthCheckResponse(status="ok")
    return response