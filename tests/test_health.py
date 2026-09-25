from app.mock_data import MQ_ONE, MQ_THREE
from tests.conftest import BASE, UNKNOWN_ID


def test_sample_patient_health(client):
    res = client.get(f"{BASE}/{MQ_ONE}/health")
    assert res.status_code == 200
    body = res.json()
    assert body["covid"]["vaccination_status"] == "Fully vaccinated"
    medical = body["medical"]
    assert medical["diagnosis"] == "AKI"
    assert medical["preferred_modality"] == "In-Center Hemo"
    resp = medical["respiratory_assessment"]
    assert resp["tracheostomy"] == "Yes - Capped"
    assert resp["requires_supplemental_oxygen"] is True
    assert resp["ventilator_dependent"] is False


def test_unvaccinated_patient_has_no_test_result(client):
    covid = client.get(f"{BASE}/{MQ_THREE}/health").json()["covid"]
    assert covid["doses"] == 0
    assert covid["last_test_result"] is None


def test_unknown_patient_returns_404(client):
    assert client.get(f"{BASE}/{UNKNOWN_ID}/health").status_code == 404
