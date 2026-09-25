from app.mock_data.insurance import INSURANCE
from app.schemas.insurance import InsuranceQuestionnaire, InsuranceResponse
from app.services.lookup import get_record


def mask_ssn(ssn: str | None) -> str | None:
    if not ssn:
        return None
    return f"***{ssn[-3:]}"


def get_insurance(patient_id: str) -> InsuranceResponse:
    record = get_record(INSURANCE, patient_id)
    answers = {k: v for k, v in record["questionnaire"].items() if k != "ssn"}
    questionnaire = InsuranceQuestionnaire(**answers, ssn_masked=mask_ssn(record["questionnaire"].get("ssn")))
    return InsuranceResponse(
        patient_id=patient_id,
        coverage=record["coverage"],
        prior_authorization=record["prior_authorization"],
        questionnaire=questionnaire,
    )
