class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name


class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, time, status="booked"):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = status

    def cancel(self):
        self.status = "cancelled"

    def update(self, new_time=None, new_practitioner=None):
        if new_time:
            self.time = new_time
        if new_practitioner:
            self.practitioner = new_practitioner


# Consistency check:
# Patient and Practitioner each hold an ID and name, matching the UML diagram.
# Appointment holds references to a Patient and Practitioner object plus
# time and status, matching the diagram's associations and multiplicities.
# No method bodies beyond cancel() and update() are implemented yet,
# per the instruction not to implement full behaviour this stage.