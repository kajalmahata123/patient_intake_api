from app.mock_data.additional_info import ADDITIONAL_INFO
from app.schemas.additional_info import AdditionalInfoResponse
from app.schemas.common import ItemStatus
from app.services.lookup import get_record


def _still_missing(items: list[dict]) -> list[dict]:
    return [item for item in items if item["status"] == ItemStatus.PENDING.value]


def get_additional_info(patient_id: str) -> AdditionalInfoResponse:
    record = get_record(ADDITIONAL_INFO, patient_id)
    return AdditionalInfoResponse(
        patient_id=patient_id,
        missing_documents=_still_missing(record["documents"]),
        missing_questionnaires=_still_missing(record["questionnaires"]),
    )
