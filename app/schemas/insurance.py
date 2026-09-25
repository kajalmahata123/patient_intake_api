"""Response model for GET /patients/{patient_id}/insurance."""

from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class AuthStatus(str, Enum):
    APPROVED = "Approved"
    PENDING = "Pending"
    DENIED = "Denied"


class Coverage(BaseModel):
    payer_name: str
    plan: str
    member_id: str
    group_number: str
    effective_date: date
    expiry_date: date


class PriorAuthorization(BaseModel):
    auth_number: str | None = None
    service: str
    status: AuthStatus
    valid_from: date | None = None
    valid_to: date | None = None


class InsuranceQuestionnaire(BaseModel):
    """Eligibility questionnaire answers captured during intake."""

    us_citizen: bool
    veteran_eligible_for_va_benefits: bool
    household_size: int
    annual_income: int
    marital_status: str
    state_of_residence: str
    years_in_current_state: int
    years_worked_and_paid_us_taxes: int
    coverage_application_submitted: date | None = None
    pending_application_last_90_days: bool
    can_provide_proof_of_state_residency: bool
    incarcerated_or_in_halfway_house: bool
    itin: str | None = None
    ssn_masked: str | None = Field(None, description="Only the last 3 digits are exposed, e.g. ***983")


class InsuranceResponse(BaseModel):
    patient_id: str
    coverage: Coverage
    prior_authorization: PriorAuthorization
    questionnaire: InsuranceQuestionnaire
