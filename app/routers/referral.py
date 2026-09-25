from fastapi import APIRouter

from app.schemas.common import ErrorResponse
from app.schemas.referral import ReferralResponse
from app.services.referral_service import get_referral

router = APIRouter(prefix="/patients", tags=["referral"])


@router.get(
    "/{patient_id}/referral",
    response_model=ReferralResponse,
    responses={404: {"model": ErrorResponse, "description": "Unknown patient_id"}},
    summary="Referral milestones, schedule and location preferences",
)
def get_referral_endpoint(patient_id: str) -> ReferralResponse:
    return get_referral(patient_id)
