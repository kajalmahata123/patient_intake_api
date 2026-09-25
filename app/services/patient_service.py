from app.mock_data.patients import PATIENTS
from app.schemas.patient import PatientResponse
from app.services.lookup import get_record


def get_patient(patient_id: str) -> PatientResponse:
    return PatientResponse(patient=get_record(PATIENTS, patient_id))
