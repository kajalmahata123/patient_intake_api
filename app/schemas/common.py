"""Shared response models."""

from datetime import date
from enum import Enum

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    detail: str


class ItemStatus(str, Enum):
    UPLOADED = "Uploaded"
    COMPLETED = "Completed"
    PENDING = "Pending"


class RequestedItem(BaseModel):
    """A document or questionnaire requested from the patient."""

    name: str
    status: ItemStatus
    requested_date: date
    completed_date: date | None = None
