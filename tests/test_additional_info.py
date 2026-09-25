from app.mock_data import MQ_ONE, MQ_THREE, MQ_TWO
from tests.conftest import BASE, UNKNOWN_ID


def test_sample_patient_missing_documents(client):
    res = client.get(f"{BASE}/{MQ_ONE}/additional-info")
    assert res.status_code == 200
    body = res.json()
    names = [d["name"] for d in body["missing_documents"]]
    assert names == [
        "Hep B Core Antibody",
        "Hep B Surface Antigen",
        "Medication & Allergy List",
        "Orders or Flowsheets",
        "Pre-Dialysis Labs",
    ]
    assert all(d["status"] == "Pending" for d in body["missing_documents"])
    assert body["missing_questionnaires"] == []


def test_complete_patient_has_nothing_missing(client):
    body = client.get(f"{BASE}/{MQ_TWO}/additional-info").json()
    assert body["missing_documents"] == []
    assert body["missing_questionnaires"] == []


def test_patient_with_missing_questionnaires(client):
    body = client.get(f"{BASE}/{MQ_THREE}/additional-info").json()
    assert len(body["missing_questionnaires"]) == 2


def test_unknown_patient_returns_404(client):
    assert client.get(f"{BASE}/{UNKNOWN_ID}/additional-info").status_code == 404
