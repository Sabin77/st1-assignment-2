appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

# --- Test calls (Part F testing) ---

# Normal appointment
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')

# Blank patient name
book_appointment('', 'Dr. Jane Roe', '2024-07-20 11:30 AM')

# Duplicate appointment (same practitioner/time as an earlier one)
book_appointment('Charlie Lee', 'Dr. John Doe', '2024-07-20 10:00 AM')

# Strange input
book_appointment(None, None, None)

print(appointments)