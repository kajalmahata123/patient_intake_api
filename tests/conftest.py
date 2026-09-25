import pytest
from fastapi.testclient import TestClient

from app.main import app

BASE = "/api/v1/patients"
UNKNOWN_ID = "000000000"


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
