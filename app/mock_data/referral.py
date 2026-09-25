from app.mock_data import MQ_ONE, MQ_THREE, MQ_TWO

DENVER_DIALYSIS = "DENVER DIALYSIS CENTER, Denver, CO"

REFERRALS: dict[str, dict] = {
    MQ_ONE: {
        "referral": {
            "referral_id": "752070773",
            "status": "Active",
            "category": "Permanent",
            "type": "NEW",
            "created": "2026-09-10",
            "last_updated": "2026-09-23",
            "treatment_start": "2026-09-10",
            "current_milestone": "Chair Held",
        },
        "milestones": [
            {"name": "Referral Received", "status": "Completed", "date": "2026-09-10", "facility": None},
            {"name": "Chair Held", "status": "In Progress", "date": "2026-09-10", "facility": DENVER_DIALYSIS},
            {"name": "Insurance Verified", "status": "Not Started", "date": None, "facility": None},
            {"name": "Admitted", "status": "Not Started", "date": None, "facility": None},
        ],
        "schedule": {
            "appointment_date": "2026-10-01",
            "appointment_time": "07:30:00",
            "provider": "Dr. Anita Rao, Nephrology",
            "status": "Tentative",
        },
        "location_preferences": {
            "preferred_facility": DENVER_DIALYSIS,
            "zip": "80205",
            "max_distance_miles": 10,
            "preferred_time_of_day": "Morning",
        },
    },
    MQ_TWO: {
        "referral": {
            "referral_id": "752070774",
            "status": "Active",
            "category": "Permanent",
            "type": "TRANSFER",
            "created": "2026-08-18",
            "last_updated": "2026-09-20",
            "treatment_start": "2026-09-15",
            "current_milestone": "Admitted",
        },
        "milestones": [
            {"name": "Referral Received", "status": "Completed", "date": "2026-08-18", "facility": None},
            {"name": "Chair Held", "status": "Completed", "date": "2026-08-25", "facility": "BOULDER HOME DIALYSIS, Boulder, CO"},
            {"name": "Insurance Verified", "status": "Completed", "date": "2026-09-01", "facility": None},
            {"name": "Admitted", "status": "Completed", "date": "2026-09-15", "facility": "BOULDER HOME DIALYSIS, Boulder, CO"},
        ],
        "schedule": {
            "appointment_date": "2026-09-29",
            "appointment_time": "14:00:00",
            "provider": "Dr. Michael Chen, Nephrology",
            "status": "Confirmed",
        },
        "location_preferences": {
            "preferred_facility": "BOULDER HOME DIALYSIS, Boulder, CO",
            "zip": "80302",
            "max_distance_miles": 15,
            "preferred_time_of_day": "Afternoon",
        },
    },
    MQ_THREE: {
        "referral": {
            "referral_id": "752070775",
            "status": "On Hold",
            "category": "Transient",
            "type": "NEW",
            "created": "2026-09-05",
            "last_updated": "2026-09-22",
            "treatment_start": None,
            "current_milestone": "Insurance Verification",
        },
        "milestones": [
            {"name": "Referral Received", "status": "Completed", "date": "2026-09-05", "facility": None},
            {"name": "Insurance Verification", "status": "In Progress", "date": "2026-09-12", "facility": None},
            {"name": "Chair Held", "status": "Not Started", "date": None, "facility": None},
        ],
        "schedule": None,
        "location_preferences": {
            "preferred_facility": "LITTLE ROCK KIDNEY CENTER, Little Rock, AR",
            "zip": "72201",
            "max_distance_miles": 25,
            "preferred_time_of_day": "Evening",
        },
    },
}
