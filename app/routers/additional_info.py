from fastapi import APIRouter

from app.schemas.common import ErrorResponse
from app.schemas.additional_info import AdditionalInfoResponse
from app.services.additional_info_service import get_additional_info

router = APIRouter(prefix="/patients", tags=["additional-info"])


@router.get(
    "/{patient_id}/additional-info",
    response_model=AdditionalInfoResponse,
    responses={404: {"model": ErrorResponse, "description": "Unknown patient_id"}},
    summary="Missing documents and missing questionnaires",
)
def get_additional_info_endpoint(patient_id: str) -> AdditionalInfoResponse:
    return get_additional_info(patient_id)
