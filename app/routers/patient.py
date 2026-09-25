from fastapi import APIRouter

from app.schemas.common import ErrorResponse
from app.schemas.patient import PatientResponse
from app.services.patient_service import get_patient

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
    responses={404: {"model": ErrorResponse, "description": "Unknown patient_id"}},
    summary="Patient info",
)
def get_patient_endpoint(patient_id: str) -> PatientResponse:
    return get_patient(patient_id)
