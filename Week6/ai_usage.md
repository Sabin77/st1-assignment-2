# AI Usage Log - Week 6

## Prompt used with Copilot
Based only on the following confirmed requirements for SmartCare, suggest
candidate classes and relationships (including whether additional classes
like managers, controllers, or services are needed). For every suggestion,
cite which requirement ID supports it. Do not invent new client requirements.

[FR-01 to FR-12 pasted from Week 5 requirements]

## Copilot's response
Copilot proposed the three core classes (Patient, Practitioner, Appointment)
each tied to specific requirement IDs, plus supporting classes:
PatientManager, PractitionerManager, AppointmentManager, and ReportService
(all marked "evidence-based"), and three optional structural classes -
TimeSlot, StatusEnum, SearchService - explicitly marked as "validation
required" rather than confirmed.

## My evaluation
I accepted the three core classes and ReportService, since these were
directly and specifically justified by requirement IDs. I rejected
PatientManager and PractitionerManager because Copilot's own justification
only showed that a *capability* was needed (e.g. "create record", "search"),
not that a *separate class* was necessary - Patient and Practitioner can
hold this themselves without an extra wrapper class. I modified
AppointmentManager, keeping the underlying idea as a lightweight helper
rather than a full class, since duplicate-booking checks (FR-05) genuinely
need logic that spans multiple appointments. I rejected TimeSlot, StatusEnum,
and SearchService, since Copilot itself flagged these as unconfirmed, and
simple types are sufficient for this stage.