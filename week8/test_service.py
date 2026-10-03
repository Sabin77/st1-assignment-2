from datetime import datetime

from appointment_repository import InMemoryAppointmentRepository
from appointment_service import AppointmentService
from domain import AppointmentStatus


# Create repository and service
repo = InMemoryAppointmentRepository()
service = AppointmentService(repo)


# -----------------------------
# TEST 1: Book first appointment
# -----------------------------

appointment1 = service.book_appointment(
    "A001",
    "P001",
    "D001",
    datetime(2026, 10, 5, 10, 0)
)

print("Test 1 - Appointment booked successfully")
print(appointment1.appointment_id)
print(appointment1.patient_id)
print(appointment1.practitioner_id)
print(appointment1.time_slot)
print()


# -----------------------------
# TEST 2: Try conflicting booking
# -----------------------------

try:
    service.book_appointment(
        "A002",
        "P002",
        "D001",
        datetime(2026, 10, 5, 10, 0)
    )
except ValueError as e:
    print("Test 2 - Conflict correctly blocked:")
    print(e)

print()


# -----------------------------
# TEST 3: Cancel first appointment
# -----------------------------

appointment1.status = AppointmentStatus.CANCELLED

print("Test 3 - First appointment cancelled")
print("Status:", appointment1.status)
print()


# -----------------------------
# TEST 4: Book same practitioner/time again
# after cancellation
# -----------------------------

appointment2 = service.book_appointment(
    "A003",
    "P003",
    "D001",
    datetime(2026, 10, 5, 10, 0)
)

print("Test 4 - Same slot booked after cancellation")
print(appointment2.appointment_id)
print(appointment2.patient_id)
print(appointment2.practitioner_id)
print(appointment2.time_slot)
print()


# -----------------------------
# TEST 5: Check repository contents
# -----------------------------

appointments = repo.get_all()

print("Test 5 - Appointments stored:", len(appointments))

for appt in appointments:
    print(
        appt.appointment_id,
        appt.patient_id,
        appt.practitioner_id,
        appt.time_slot,
        appt.status
    )