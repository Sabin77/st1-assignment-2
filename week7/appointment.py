from enum import Enum, auto
from datetime import datetime


class AppointmentStatus(Enum):
    BOOKED = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class Appointment:
    def __init__(self, appointment_id: str, patient_id: str, practitioner_id: str, time_slot: datetime,
                 status: AppointmentStatus = AppointmentStatus.BOOKED):
        if not patient_id:
            raise ValueError("Patient ID cannot be empty")
        if not practitioner_id:
            raise ValueError("Practitioner ID cannot be empty")
        if not isinstance(time_slot, datetime):
            raise ValueError("time_slot must be a datetime object")

        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.practitioner_id = practitioner_id
        self.time_slot = time_slot
        self.status = status

    def cancel(self) -> None:
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled.")
        if self.status == AppointmentStatus.COMPLETED:
            raise ValueError("Completed appointments cannot be cancelled.")
        self.status = AppointmentStatus.CANCELLED

    def update(self, new_time: datetime = None, new_practitioner_id: str = None) -> None:
        if self.status == AppointmentStatus.COMPLETED:
            raise ValueError("Completed appointments cannot be modified.")
        if new_time:
            self.time_slot = new_time
        if new_practitioner_id:
            self.practitioner_id = new_practitioner_id


a = Appointment("A001", "P001", "D001", datetime(2024, 7, 20, 10, 0))
print("Created:", a.status)

a.cancel()
print("After first cancel:", a.status)

try:
    a.cancel()  # should now raise an error
except ValueError as e:
    print("Error on second cancel:", e)

try:
    bad = Appointment("A002", "", "D001", "not-a-date")
except ValueError as e:
    print("Error on bad input:", e)