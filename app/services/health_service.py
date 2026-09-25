from app.mock_data.health import HEALTH
from app.schemas.health import HealthResponse
from app.services.lookup import get_record


def get_health(patient_id: str) -> HealthResponse:
    return HealthResponse(patient_id=patient_id, **get_record(HEALTH, patient_id))
