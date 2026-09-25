"""Response model for GET /patients/{patient_id}/health."""

from datetime import date
from enum import Enum

from pydantic import BaseModel


class VaccinationStatus(str, Enum):
    FULLY_VACCINATED = "Fully vaccinated"
    PARTIALLY_VACCINATED = "Partially vaccinated"
    NOT_VACCINATED = "Not vaccinated"


class TestResult(str, Enum):
    NEGATIVE = "Negative"
    POSITIVE = "Positive"


class Covid(BaseModel):
    vaccination_status: VaccinationStatus
    doses: int
    last_test_result: TestResult | None = None
    last_test_date: date | None = None


class Medication(BaseModel):
    name: str
    dosage: str
    frequency: str


class RespiratoryAssessment(BaseModel):
    tracheostomy: str
    ambulatory: bool
    effective_cough: bool
    requires_suctioning: bool
    requires_supplemental_oxygen: bool
    ventilator_dependent: bool
    pulmonary_infection_last_30_days: bool
    currently_on_antibiotic: bool
    lvad_patient: bool


class Medical(BaseModel):
    diagnosis: str
    preferred_modality: str
    conditions: list[str]
    allergies: list[str]
    current_medications: list[Medication]
    respiratory_assessment: RespiratoryAssessment


class HealthResponse(BaseModel):
    patient_id: str
    covid: Covid
    medical: Medical
