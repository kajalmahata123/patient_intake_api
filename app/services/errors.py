class PatientNotFoundError(Exception):
    def __init__(self, patient_id: str) -> None:
        self.patient_id = patient_id
        super().__init__(f"Patient '{patient_id}' not found")
