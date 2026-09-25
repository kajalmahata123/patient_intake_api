from app.mock_data import MQ_ONE, MQ_THREE, MQ_TWO


def _uploaded(name: str, requested: str, completed: str) -> dict:
    return {"name": name, "status": "Uploaded", "requested_date": requested, "completed_date": completed}


def _pending(name: str, requested: str) -> dict:
    return {"name": name, "status": "Pending", "requested_date": requested, "completed_date": None}


ADDITIONAL_INFO: dict[str, dict] = {
    MQ_ONE: {
        "documents": [
            _uploaded("Face Sheet", "2026-09-10", "2026-09-23"),
            _uploaded("Hep B Surface Antibody", "2026-09-10", "2026-09-23"),
            _uploaded("History and Physical", "2026-09-10", "2026-09-23"),
            _uploaded("Nephrology Note", "2026-09-10", "2026-09-23"),
            _uploaded("Tuberculosis Test (TB)", "2026-09-10", "2026-09-23"),
            _pending("Hep B Core Antibody", "2026-09-10"),
            _pending("Hep B Surface Antigen", "2026-09-10"),
            _pending("Medication & Allergy List", "2026-09-10"),
            _pending("Orders or Flowsheets", "2026-09-10"),
            _pending("Pre-Dialysis Labs", "2026-09-10"),
        ],
        "questionnaires": [
            {"name": "Insurance Eligibility", "status": "Completed", "requested_date": "2026-09-10", "completed_date": "2026-09-21"},
        ],
    },
    MQ_TWO: {
        "documents": [
            _uploaded("Face Sheet", "2026-08-18", "2026-08-20"),
            _uploaded("History and Physical", "2026-08-18", "2026-08-20"),
            _uploaded("Pre-Dialysis Labs", "2026-08-18", "2026-08-22"),
        ],
        "questionnaires": [
            {"name": "Insurance Eligibility", "status": "Completed", "requested_date": "2026-08-18", "completed_date": "2026-08-19"},
            {"name": "Home Dialysis Readiness", "status": "Completed", "requested_date": "2026-08-18", "completed_date": "2026-08-24"},
        ],
    },
    MQ_THREE: {
        "documents": [
            _uploaded("Face Sheet", "2026-09-05", "2026-09-06"),
            _pending("Nephrology Note", "2026-09-05"),
            _pending("Proof of State Residency", "2026-09-12"),
        ],
        "questionnaires": [
            _pending("Insurance Eligibility", "2026-09-05"),
            _pending("Peritoneal Dialysis Training Readiness", "2026-09-12"),
        ],
    },
}
