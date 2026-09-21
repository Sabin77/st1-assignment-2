# SmartCare v0.2 - Requirements Specification

## 1. Problem and Scope

SmartCare is a small community clinic currently managing patients and appointments
through spreadsheets, paper records, and manual processes. This has caused duplicate
bookings, difficulty locating patient records, inconsistent appointment status,
limited visibility of practitioner availability, manual cancellation processes,
unreliable appointment history, and difficulty producing operational reports.
Management wants a simple, maintainable system supporting patient, practitioner,
and appointment management — explicitly not a complex hospital information system.

**In Scope:** patient record management, practitioner record management, appointment
booking/cancellation/status tracking, appointment history retention, basic
operational reporting (provisional).

**Out of Scope:** online payment processing, facial recognition or biometric login,
AI-generated treatment recommendations, insurance processing, full hospital
information system features.

## 2. Stakeholders

| Stakeholder | Need | Evidence |
| --- | --- | --- |
| Receptionist | Search patients, book/cancel appointments without duplicates | "duplicate appointment bookings," "manual cancellation processes" |
| Patient | Accurate appointment record and history | "difficulty locating patient records," "lack of reliable appointment history" |
| Practitioner (GP) | View own schedule/availability | "limited visibility of practitioner availability" |
| Clinic manager | Operational reports, overall reliability | "difficulty producing basic operational reports" |

## 3. Functional Requirements

FR-01: The system shall allow staff to create a new patient record.
FR-02: The system shall allow staff to search for a patient by name or ID.
FR-03: The system shall allow staff to create a new practitioner record.
FR-04: The system shall allow staff to book a new appointment linking a patient, practitioner, and time slot.
FR-05: The system shall prevent booking two appointments for the same practitioner at the same time.
FR-06: The system shall allow staff to cancel an existing appointment.
FR-07: The system shall retain a record of cancelled appointments rather than deleting them.
FR-08: The system shall display each appointment's current status (e.g. booked, completed, cancelled).
FR-09: The system shall allow a practitioner to view their own upcoming appointments.
FR-10: The system shall allow staff to view a patient's full appointment history.
FR-11: The system shall allow staff to update an existing appointment's time or practitioner.
FR-12: The system shall generate a basic report of appointments over a given date range.

## 4. Non-Functional Requirements

NFR-01: The system shall not lose stored appointment data if the program closes unexpectedly. (Reliability)
NFR-02: A new receptionist shall be able to book an appointment without external training, using on-screen prompts only. (Usability)
NFR-03: Core booking logic shall be separated from display/output code so it can be modified without rewriting the whole program. (Maintainability)
NFR-04: The system shall not allow an appointment to be saved with a missing patient, practitioner, or time value. (Data integrity)
NFR-05: Core functions (e.g. booking, cancellation) shall be independently testable without running the full program interactively. (Testability)
NFR-06: The system shall return patient search results within 2 seconds for a dataset of up to 500 records. (Performance)

## 5. User Stories

US-01: As a receptionist, I want to search for a patient by name, so that I can quickly find their record without scrolling through a full list.
US-02: As a receptionist, I want to be warned about duplicate bookings, so that I don't accidentally double-book a practitioner.
US-03: As a practitioner, I want to view my own schedule, so that I know my upcoming appointments without asking reception.
US-04: As a receptionist, I want to cancel an appointment, so that the time slot becomes available again.
US-05: As a clinic manager, I want to see a report of appointments over a date range, so that I can review clinic activity.
US-06: As a receptionist, I want to view a patient's appointment history, so that I have accurate context before their visit.

## 6. Acceptance Criteria

GIVEN a practitioner already has an appointment at 10:00 AM on a given date
WHEN a receptionist tries to book another appointment for the same practitioner at 10:00 AM that date
THEN the system shall reject the booking and display a duplicate-booking warning

GIVEN an existing booked appointment
WHEN a receptionist selects that appointment and confirms cancellation
THEN the system shall change its status to "cancelled" and retain it in history rather than deleting it

GIVEN a patient named "Alice Smith" exists in the system
WHEN a receptionist searches for "Alice"
THEN the system shall return Alice Smith's record in the results

## 7. Assumptions and Open Questions

- What minimum fields must appear in a "basic" operational report?
- Should appointment status values be limited to a fixed list (e.g. booked, completed, cancelled), and who is responsible for marking an appointment "completed"?
- Is reporting a mandatory v0.2 feature or genuinely provisional pending client confirmation?
- What storage mechanism will be used to persist data (file-based or lightweight database)?
- Should cancellation reasons be recorded alongside a cancelled appointment?
- What is the expected format for appointment time (e.g. 24-hour, includes date, timezone)?

## 8. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
| "Basic operational reporting" is undefined (no field/format spec) | Assumption | Accepted | Valid gap — the brief only says "basic," no detail given | Moved to open questions (section 7); needs client input on report fields |
| FR-08 status categories aren't a fixed, defined list | Assumption | Accepted | FR-08 gives examples, not a closed set — could cause inconsistent implementation | Moved to open questions (section 7); propose fixed list (booked/completed/cancelled) for client to confirm |
| FR-02 search behavior (partial match, case-insensitive) isn't stated in the requirement itself | Evidence (matches US-01) | Modified | US-01 already implies partial matching ("Alice" finds "Alice Smith"), so this should be explicit in the requirement, not just implied by the story | FR-02 reworded to: "The system shall allow staff to search for a patient by full or partial name match (case-insensitive) or by ID." |
| FR-12 report requirement isn't marked provisional, but scope lists reporting as provisional | Evidence (direct contradiction within the document) | Accepted | Genuine inconsistency between section 1 (scope) and section 3 (FR-12) | Moved to open questions (section 7) pending confirmation of whether reporting is mandatory or provisional |
| Persistence mechanism (file vs. database) is unspecified | Evidence (NFR-01 requires persistence but no mechanism is defined) | Accepted | Fair gap — "simple system" and "must persist data" are in tension without a defined storage approach | Moved to open questions (section 7) as a technical decision |
| Practitioner identity/authentication isn't defined | Assumption | Rejected (for v0.2) | Reasonable point, but authentication/login is a security feature beyond this stage's scope for a "simple, maintainable system" | Noted as a future-stage consideration, not added to v0.2 open questions |

