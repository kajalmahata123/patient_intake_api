"""Shared mock-store lookup. Replace with repository calls when a DB is added."""

from typing import Any

from app.services.errors import PatientNotFoundError


def get_record(store: dict[str, dict[str, Any]], patient_id: str) -> dict[str, Any]:
    record = store.get(patient_id)
    if record is None:
        raise PatientNotFoundError(patient_id)
    return record
