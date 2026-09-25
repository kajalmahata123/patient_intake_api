# Patient Intake Mock API

Read-only FastAPI service with five mock endpoints, one per intake section. There is no database;
data lives in `app/mock_data/` behind `app/services/` (router → service → mock data), so a real
database later changes only the service layer.

## Prerequisites

- Python 3.11 or newer (`python3 --version`)
- git

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/kajalmahata123/patient_intake_api.git
cd patient_intake_api
```

### 2. Create and activate a virtual environment

Always work inside a virtual environment so the project's packages don't touch your system Python.

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Once it is active, your prompt starts with `(.venv)`. Run `deactivate` to leave it.

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run the server

With the virtual environment active:

```bash
uvicorn app.main:app --reload
```

- API base: http://127.0.0.1:8000/api/v1
- Swagger UI: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

`--reload` restarts the server when code changes. Stop it with `Ctrl+C`.

## Run the tests

```bash
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

## Try it with curl

```bash
BASE=http://127.0.0.1:8000/api/v1/patients

curl -s $BASE/752070773                 | python3 -m json.tool
curl -s $BASE/752070773/insurance       | python3 -m json.tool
curl -s $BASE/752070773/health          | python3 -m json.tool
curl -s $BASE/752070773/referral        | python3 -m json.tool
curl -s $BASE/752070773/additional-info | python3 -m json.tool

# Unknown patient -> 404
curl -s -w "\n%{http_code}\n" $BASE/000000000
```

## Project structure

```
app/
  main.py          App setup, router registration, 404 handler
  routers/         One file per API
  schemas/         Pydantic response models (shown in Swagger)
  services/        Looks up mock data by patient_id, masks SSN, filters missing items
  mock_data/       Mock records keyed by patient_id
tests/             One test file per endpoint
```

## Troubleshooting

- **`command not found: uvicorn` or `pytest`**: the virtual environment isn't active. Run
  `source .venv/bin/activate` (Windows: `.venv\Scripts\Activate.ps1`).
- **`Address already in use` on port 8000**: another process holds the port. Use a different
  one with `uvicorn app.main:app --reload --port 8001`, or find the process with `lsof -i :8000`.
- **PowerShell blocks `Activate.ps1`**: run
  `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then activate again.
