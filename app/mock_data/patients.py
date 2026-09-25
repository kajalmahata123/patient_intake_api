from app.mock_data import MQ_ONE, MQ_THREE, MQ_TWO

PATIENTS: dict[str, dict] = {
    MQ_ONE: {
        "patient_id": MQ_ONE,
        "first_name": "Test",
        "last_name": "MQOne",
        "date_of_birth": "1945-09-09",
        "gender": "Male",
        "phone": "(765) 768-3487",
        "email": "test.mqone@example.com",
        "address": {"line1": "3241 Clayton Street", "city": "Denver", "state": "CO", "zip": "80205"},
    },
    MQ_TWO: {
        "patient_id": MQ_TWO,
        "first_name": "Test",
        "last_name": "MQTwo",
        "date_of_birth": "1958-03-14",
        "gender": "Female",
        "phone": "(303) 555-0142",
        "email": "test.mqtwo@example.com",
        "address": {"line1": "1180 Pearl Street", "city": "Boulder", "state": "CO", "zip": "80302"},
    },
    MQ_THREE: {
        "patient_id": MQ_THREE,
        "first_name": "Test",
        "last_name": "MQThree",
        "date_of_birth": "1962-11-27",
        "gender": "Male",
        "phone": "(501) 555-0199",
        "email": None,
        "address": {"line1": "402 W Markham Street", "city": "Little Rock", "state": "AR", "zip": "72201"},
    },
}
