from fastapi import APIRouter

from app.schemas.common import ErrorResponse
from app.schemas.insurance import InsuranceResponse
from app.services.insurance_service import get_insurance

router = APIRouter(prefix="/patients", tags=["insurance"])


@router.get(
    "/{patient_id}/insurance",
    response_model=InsuranceResponse,
    responses={404: {"model": ErrorResponse, "description": "Unknown patient_id"}},
    summary="Prior authorization, coverage and eligibility questionnaire",
)
def get_insurance_endpoint(patient_id: str) -> InsuranceResponse:
    return get_insurance(patient_id)
