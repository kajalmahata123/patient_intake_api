"""Response model for GET /patients/{patient_id}/referral."""

import datetime as dt
from enum import Enum

from pydantic import BaseModel


class MilestoneStatus(str, Enum):
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"
    NOT_STARTED = "Not Started"


class Milestone(BaseModel):
    name: str
    status: MilestoneStatus
    date: dt.date | None = None
    facility: str | None = None


class Schedule(BaseModel):
    appointment_date: dt.date
    appointment_time: dt.time
    provider: str
    status: str


class LocationPreferences(BaseModel):
    preferred_facility: str
    zip: str
    max_distance_miles: int
    preferred_time_of_day: str


class ReferralSummary(BaseModel):
    referral_id: str
    status: str
    category: str
    type: str
    created: dt.date
    last_updated: dt.date
    treatment_start: dt.date | None = None
    current_milestone: str


class ReferralResponse(BaseModel):
    patient_id: str
    referral: ReferralSummary
    milestones: list[Milestone]
    schedule: Schedule | None = None
    location_preferences: LocationPreferences
