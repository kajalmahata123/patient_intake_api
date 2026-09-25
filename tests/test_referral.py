from app.mock_data import MQ_ONE, MQ_THREE
from tests.conftest import BASE, UNKNOWN_ID


def test_sample_referral(client):
    res = client.get(f"{BASE}/{MQ_ONE}/referral")
    assert res.status_code == 200
    body = res.json()
    ref = body["referral"]
    assert ref["referral_id"] == "752070773"
    assert (ref["status"], ref["category"], ref["type"]) == ("Active", "Permanent", "NEW")
    assert ref["current_milestone"] == "Chair Held"
    chair_held = next(m for m in body["milestones"] if m["name"] == "Chair Held")
    assert chair_held["facility"] == "DENVER DIALYSIS CENTER, Denver, CO"
    assert chair_held["date"] == "2026-09-10"
    assert body["location_preferences"]["preferred_facility"] == "DENVER DIALYSIS CENTER, Denver, CO"


def test_on_hold_referral_has_no_schedule(client):
    body = client.get(f"{BASE}/{MQ_THREE}/referral").json()
    assert body["referral"]["status"] == "On Hold"
    assert body["schedule"] is None


def test_unknown_patient_returns_404(client):
    assert client.get(f"{BASE}/{UNKNOWN_ID}/referral").status_code == 404
