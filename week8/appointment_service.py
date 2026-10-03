from domain import Appointment, AppointmentStatus
from appointment_repository import AppointmentRepository


class AppointmentService:
    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def book_appointment(
        self,
        appointment_id,
        patient_id,
        practitioner_id,
        time_slot
    ):
        appointments = self.repository.get_all()

        for appt in appointments:
            if (
                appt.practitioner_id == practitioner_id
                and appt.time_slot == time_slot
                and appt.status != AppointmentStatus.CANCELLED
            ):
                raise ValueError(
                    "This practitioner already has an appointment at this time."
                )

        appointment = Appointment(
            appointment_id,
            patient_id,
            practitioner_id,
            time_slot
        )

        self.repository.add(appointment)

        return appointment