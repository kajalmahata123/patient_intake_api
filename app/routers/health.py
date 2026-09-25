from fastapi import APIRouter

from app.schemas.common import ErrorResponse
from app.schemas.health import HealthResponse
from app.services.health_service import get_health

router = APIRouter(prefix="/patients", tags=["health"])


@router.get(
    "/{patient_id}/health",
    response_model=HealthResponse,
    responses={404: {"model": ErrorResponse, "description": "Unknown patient_id"}},
    summary="COVID and medical info",
)
def get_health_endpoint(patient_id: str) -> HealthResponse:
    return get_health(patient_id)
