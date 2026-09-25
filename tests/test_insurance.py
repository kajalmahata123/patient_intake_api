from app.mock_data import MQ_ONE, MQ_TWO
from app.services.insurance_service import mask_ssn
from tests.conftest import BASE, UNKNOWN_ID


def test_sample_patient_has_pending_auth_and_questionnaire(client):
    res = client.get(f"{BASE}/{MQ_ONE}/insurance")
    assert res.status_code == 200
    body = res.json()
    assert body["prior_authorization"]["status"] == "Pending"
    q = body["questionnaire"]
    assert q["household_size"] == 3
    assert q["state_of_residence"] == "Arkansas"
    assert q["coverage_application_submitted"] == "2026-09-21"
    assert q["itin"] == "12121"


def test_ssn_is_masked_and_raw_value_never_returned(client):
    res = client.get(f"{BASE}/{MQ_ONE}/insurance")
    q = res.json()["questionnaire"]
    assert q["ssn_masked"] == "***983"
    assert "ssn" not in q
    assert "192983" not in res.text


def test_approved_patient(client):
    auth = client.get(f"{BASE}/{MQ_TWO}/insurance").json()["prior_authorization"]
    assert auth["status"] == "Approved"
    assert auth["auth_number"] == "PA-2026-118834"


def test_mask_ssn_handles_missing_value():
    assert mask_ssn(None) is None
    assert mask_ssn("") is None


def test_unknown_patient_returns_404(client):
    assert client.get(f"{BASE}/{UNKNOWN_ID}/insurance").status_code == 404
