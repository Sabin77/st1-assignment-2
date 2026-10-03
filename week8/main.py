from datetime import datetime
from appointment_repository import InMemoryAppointmentRepository
from appointment_service import AppointmentService

# Create repository
repo = InMemoryAppointmentRepository()

# Create service using the repository
service = AppointmentService(repo)

# Book an example appointment
appointment = service.book_appointment(
    "A001",
    "P001",
    "D001",
    datetime(2026, 10, 5, 10, 0)
)

# Display confirmation
print("Appointment booked successfully!")
print("Appointment ID:", appointment.appointment_id)
print("Patient ID:", appointment.patient_id)
print("Practitioner ID:", appointment.practitioner_id)
print("Time:", appointment.time_slot)