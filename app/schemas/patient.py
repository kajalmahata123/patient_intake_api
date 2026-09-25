"""Response model for GET /patients/{patient_id}."""

from datetime import date

from pydantic import BaseModel


class Address(BaseModel):
    line1: str
    city: str
    state: str
    zip: str


class Patient(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone: str
    email: str | None = None
    address: Address


class PatientResponse(BaseModel):
    patient: Patient
