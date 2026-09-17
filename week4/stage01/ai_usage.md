# AI Usage Log

## Part C prompt (used with Microsoft Copilot)
Act as a Python tutor. I am learning introductory software technology.
Here is a small appointment-booking function. [pasted my book_appointment/display_appointments code]
1. Explain what the code does.
2. Identify three limitations.
3. Suggest improvements.
4. Do not rewrite the whole application.
5. Ask me two questions to test my understanding.

## Copilot's questions and my answers
**Q1: What Python data structure is used to store multiple appointments, and why is it suitable?**

appointments is a list, and each individual appointment inside it is a dictionary. So really it's "a list of dictionaries."

The list (appointments = [ ]) is suitable because you don't know in advance how many appointments will be booked, a list can grow dynamically as book_appointment() is called again and again, just by appending to it.
Each dictionary ({"patient": ..., "practitioner": ..., "time": ...}) is suitable because one appointment has several related pieces of information that need clear labels. A dictionary lets you access each piece by name (appointment['patient']) instead of having to remember "the name is always item 0, the time is always item 2," which would be easy to mix up.

**Q2: What happens inside the book_appointment() function each time it is called?**
Walking through it step by step, e.g. book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM'):

The three arguments get assigned to the parameters patient_name, practitioner_name, appointment_time.
It checks if not patient_name: — if the patient name is empty (or None), it immediately stops the function and raises a ValueError, so no bad appointment gets recorded.
If the name is fine, it builds a new dictionary called appointment with three key-value pairs: "patient", "practitioner", and "time", using the values passed in.
That new dictionary is appended to the appointments list with appointments.append(appointment) — so it's now stored alongside any previous appointments.
The function doesn't print or return anything itself — it just silently stores the data, which is why you need display_appointments() separately to see it.

## Part D prompt
Create a simple beginner-friendly Python function that stores patient name,
practitioner name and appointment time. Do not use a database or a GUI.

## Copilot's Part D response
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
