class Patient:
    def __init__(self, patient_id: str, name: str):
        if not name:
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name

p = Patient("P001", "")
print(p.patient_id)
print(p.name)