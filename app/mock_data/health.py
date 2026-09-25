from app.mock_data import MQ_ONE, MQ_THREE, MQ_TWO

HEALTH: dict[str, dict] = {
    MQ_ONE: {
        # The sample record has no COVID data, so these values are invented.
        "covid": {
            "vaccination_status": "Fully vaccinated",
            "doses": 3,
            "last_test_result": "Negative",
            "last_test_date": "2026-09-08",
        },
        "medical": {
            "diagnosis": "AKI",
            "preferred_modality": "In-Center Hemo",
            "conditions": ["Acute kidney injury", "Hypertension"],
            "allergies": ["Penicillin"],
            "current_medications": [
                {"name": "Amlodipine", "dosage": "5 mg", "frequency": "Once daily"},
                {"name": "Sevelamer", "dosage": "800 mg", "frequency": "Three times daily with meals"},
            ],
            "respiratory_assessment": {
                "tracheostomy": "Yes - Capped",
                "ambulatory": True,
                "effective_cough": True,
                "requires_suctioning": True,
                "requires_supplemental_oxygen": True,
                "ventilator_dependent": False,
                "pulmonary_infection_last_30_days": False,
                "currently_on_antibiotic": False,
                "lvad_patient": False,
            },
        },
    },
    MQ_TWO: {
        "covid": {
            "vaccination_status": "Fully vaccinated",
            "doses": 4,
            "last_test_result": "Negative",
            "last_test_date": "2026-08-30",
        },
        "medical": {
            "diagnosis": "ESRD",
            "preferred_modality": "Home Hemo",
            "conditions": ["End-stage renal disease", "Type 2 diabetes"],
            "allergies": [],
            "current_medications": [
                {"name": "Insulin glargine", "dosage": "20 units", "frequency": "Nightly"},
                {"name": "Calcitriol", "dosage": "0.25 mcg", "frequency": "Once daily"},
            ],
            "respiratory_assessment": {
                "tracheostomy": "No",
                "ambulatory": True,
                "effective_cough": True,
                "requires_suctioning": False,
                "requires_supplemental_oxygen": False,
                "ventilator_dependent": False,
                "pulmonary_infection_last_30_days": False,
                "currently_on_antibiotic": False,
                "lvad_patient": False,
            },
        },
    },
    MQ_THREE: {
        "covid": {
            "vaccination_status": "Not vaccinated",
            "doses": 0,
            "last_test_result": None,
            "last_test_date": None,
        },
        "medical": {
            "diagnosis": "CKD Stage 5",
            "preferred_modality": "Peritoneal Dialysis",
            "conditions": ["Chronic kidney disease stage 5", "Congestive heart failure"],
            "allergies": ["Sulfa drugs", "Latex"],
            "current_medications": [
                {"name": "Furosemide", "dosage": "40 mg", "frequency": "Twice daily"},
            ],
            "respiratory_assessment": {
                "tracheostomy": "No",
                "ambulatory": False,
                "effective_cough": True,
                "requires_suctioning": False,
                "requires_supplemental_oxygen": True,
                "ventilator_dependent": False,
                "pulmonary_infection_last_30_days": True,
                "currently_on_antibiotic": True,
                "lvad_patient": False,
            },
        },
    },
}
