from app.mock_data.referral import REFERRALS
from app.schemas.referral import ReferralResponse
from app.services.lookup import get_record


def get_referral(patient_id: str) -> ReferralResponse:
    return ReferralResponse(patient_id=patient_id, **get_record(REFERRALS, patient_id))
