# Patient Intake Mock API

Read-only FastAPI service with five mock endpoints, one per intake section. No database;
data lives in `app/mock_data/` behind `app/services/` (router → service → mock data).

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload       # Swagger: http://localhost:8000/docs
pytest -q
```

## Endpoints (all `GET`, under `/api/v1`)

| Path | Returns |
|---|---|
| `/patients/{patient_id}` | patient |
| `/patients/{patient_id}/insurance` | coverage, prior_authorization, questionnaire (SSN masked) |
| `/patients/{patient_id}/health` | covid, medical (incl. respiratory assessment) |
| `/patients/{patient_id}/referral` | referral summary, milestones, schedule, location_preferences |
| `/patients/{patient_id}/additional-info` | missing_documents, missing_questionnaires (pending items only) |

Unknown `patient_id` → `404 {"detail": "Patient '<id>' not found"}`.

## Mock patients

| patient_id | Name | State |
|---|---|---|
| `752070773` | Test MQOne | Sample record from the meeting notes: pending auth, 5 missing docs |
| `752070774` | Test MQTwo | Approved auth, nothing missing |
| `752070775` | Test MQThree | Denied auth, referral on hold, no schedule, 2 missing questionnaires |
