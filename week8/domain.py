from enum import Enum, auto
from datetime import datetime


class AppointmentStatus(Enum):
    BOOKED = auto()
    COMPLETED = auto()
    CANCELLED = auto()


class Patient:
    def __init__(self, patient_id: str, name: str):
        if not name:
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not name:
            raise ValueError("Practitioner name cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty


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

        if new_time is not None:
            if not isinstance(new_time, datetime):
                raise ValueError("new_time must be a datetime object")
            self.time_slot = new_time

        if new_practitioner_id is not None:
            if not new_practitioner_id:
                raise ValueError("new_practitioner_id cannot be empty")
            self.practitioner_id = new_practitioner_id