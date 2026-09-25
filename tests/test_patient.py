from app.mock_data import MQ_ONE
from tests.conftest import BASE, UNKNOWN_ID


def test_returns_sample_patient(client):
    res = client.get(f"{BASE}/{MQ_ONE}")
    assert res.status_code == 200
    patient = res.json()["patient"]
    assert patient["first_name"] == "Test"
    assert patient["last_name"] == "MQOne"
    assert patient["date_of_birth"] == "1945-09-09"
    assert patient["gender"] == "Male"
    assert patient["phone"] == "(765) 768-3487"
    assert patient["address"] == {"line1": "3241 Clayton Street", "city": "Denver", "state": "CO", "zip": "80205"}


def test_unknown_patient_returns_404(client):
    res = client.get(f"{BASE}/{UNKNOWN_ID}")
    assert res.status_code == 404
    assert res.json() == {"detail": f"Patient '{UNKNOWN_ID}' not found"}
