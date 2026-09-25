"""Response model for GET /patients/{patient_id}/additional-info."""

from pydantic import BaseModel

from app.schemas.common import RequestedItem


class AdditionalInfoResponse(BaseModel):
    patient_id: str
    missing_documents: list[RequestedItem]
    missing_questionnaires: list[RequestedItem]
