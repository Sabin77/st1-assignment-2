# SmartCare v0.4 - Domain Implementation Workbook

## Tutorial Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
| --- | --- | --- |
| Patient | name should never be empty | get name, get ID |
| Practitioner | name and specialty should never be empty | get name, get specialty |
| Appointment | status must only change through valid transitions | cancel(), reschedule(), get status |

## Tutorial Activity 2 - Composition or Inheritance?

| Relationship | Decision | Reason |
| --- | --- | --- |
| Appointment <-> Patient | Association | An appointment references a patient but isn't "a type of" patient |
| Appointment <-> Practitioner | Association | Same reasoning |
| Doctor <-> Practitioner (hypothetical) | Inheritance | A Doctor IS a type of Practitioner - a specialization |
| Clinic <-> Appointment | Association | A clinic may track appointments but doesn't need to own their lifecycle |

## Tutorial Activity 3 - Responsibility Allocation

- Who decides if SCHEDULED can become CANCELLED? The Appointment object itself, through a controlled method.
- Who validates a patient name? The Patient class itself, in its own constructor.
- Should Appointment execute SQL? No - database access is an infrastructure concern.
- Should the UI decide legal status transitions? No - business rules belong in the domain layer.

## Tutorial Activity 4 - AI Code Critique
The AI-generated Appointment class has the following design problems:

1. **Public status mutation** - The status field can be set directly from
   outside the class (e.g. `appointment.status = "cancelled"`), which
   breaks encapsulation. Anyone can set an appointment to any status,
   bypassing the rule that only certain transitions should be allowed.
   Fix: keep status private/protected, and only allow changes through a
   controlled method like `cancel()`.

2. **SQL inside cancel()** - The method directly executes a database query
   (e.g. an UPDATE statement) inside the domain class. Fix: a domain class
   should not know about databases; persistence is a separate concern.
   cancel() should only update the object's own state.

3. **NotificationManager dependency** - The class depends on a
   NotificationManager to send notifications. Fix: no requirement in the
   v0.2 brief mentioned notifications, so this is scope creep and should
   be removed entirely.

4. **Inheritance from PatientRecord** - The class is written as
   `class Appointment(PatientRecord)`, treating Appointment as a type of
   patient record. Fix: this should be association, not inheritance - an
   Appointment references a Patient, it is not a kind of Patient.

5. **No validation on state transitions** - The class does not check
   whether a transition is legal before allowing it (e.g. cancelling an
   already-cancelled appointment). Fix: cancel() should check the current
   status first and raise an error if the transition is not allowed.

## Exit Question

Code can be object-oriented syntactically but still have poor
object-oriented design because using classes and methods is only syntax -
it does not guarantee that good design principles are being followed. The
example Appointment class technically is a Python class with methods, so
it looks object-oriented, but it violates encapsulation (public status
mutation), mixes unrelated responsibilities together (SQL and
notifications inside a domain class), and models a relationship
incorrectly (inheritance instead of association). Good object-oriented
design is about how well the code reflects real relationships and
protects the integrity of its data, not just which keywords are used.


## Part A - Revisit Approved UML

Before implementation, I confirmed the approved UML from Week 6:
- Patient: patient_id, name; get_details()
- Practitioner: practitioner_id, name; get_schedule()
- Appointment: appointment_id, time, status; cancel(), update()
- Patient and Practitioner each associate with Appointment (one-to-many),
  not inheritance.

These responsibilities and relationships were used as the basis for the
implementation below.

## Part B - Implement Patient (AI OFF)

Implemented independently, without AI assistance. The class stores
patient_id and name with type hints, and validates that name is not
empty, raising a ValueError if it is.

Tested manually:
- Patient("P001", "Alice Smith") -> created successfully, name printed
  correctly.
- Patient("P002", "") -> raised ValueError: "Patient name cannot be
  empty", as expected.

## Part C - Implement Practitioner (AI OFF)

Implemented independently, without AI assistance, following the same
pattern as Patient. The class stores practitioner_id, name, and
specialty with type hints, and validates that name is not empty.

Tested manually:
- Practitioner("D001", "Dr. John Doe", "General Practice") -> created
  successfully, all fields printed correctly.
- Practitioner("D002", "", "Pediatrics") -> raised ValueError:
  "Practitioner name cannot be empty", as expected.

## Part D - Implement Appointment (AI ON)

Implemented using Copilot, as required by this part of the lab. Copilot was
given the approved Appointment UML (appointment_id, time, status; cancel()
and update() operations, association with Patient and Practitioner) along
with the confirmed FR-04 to FR-12 requirements, and the explicit
constraints from the handout: no database, UI, notification, or service
classes; protect status transitions; use type hints and an
AppointmentStatus enum.

### Prompt used

Act as a Python pair programmer. Implement only the Appointment class from
the approved SmartCare UML. Use type hints and an AppointmentStatus enum.
Cancelled appointments remain as objects. Do not add database, UI,
notification or service classes. Protect status transitions and explain
any decision not directly visible in the UML.

UML: Appointment has appointment_id, time, status; operations cancel() and
update(). Associates with Patient and Practitioner (one-to-many,
association not inheritance).

### Copilot's contribution

Copilot generated an AppointmentStatus enum (BOOKED, COMPLETED, CANCELLED)
and an Appointment class implemented as a dataclass, with four methods:
cancel(), reschedule(), change_practitioner(), and mark_completed(). It
also explained several design decisions not shown in the UML, including
blocking transitions out of COMPLETED, and allowing a CANCELLED
appointment to be rescheduled back to BOOKED.

The full generated code and explanation are recorded in ai_usage.md. This
output was reviewed in Part E before being accepted, modified, or
rejected.

## Part E - Review Generated Code

Reviewed Copilot's generated Appointment class against the approved UML
and the constraints given in the prompt.

1. **Public state mutation - still a problem.** Copilot's explanation
   claims direct assignment is "discouraged," but the class is a
   dataclass with plain public fields. Nothing actually prevents
   `appointment.status = AppointmentStatus.CANCELLED` from outside the
   class, bypassing every check inside cancel(). This is the same public
   status mutation flaw identified in the Tutorial's AI Code Critique.

2. **Model inconsistency with the approved UML.** The approved UML has
   Appointment holding references to actual Patient and Practitioner
   objects (association). Copilot instead used patient_id and
   practitioner_id as plain strings, not object references. This does not
   match the agreed design.

3. **Unsupported/invented features beyond the UML.** The UML only
   specified cancel() and update(). Copilot invented reschedule(),
   change_practitioner(), and mark_completed() instead, none of which
   were in the approved model, expanding scope beyond what was agreed.

4. **An unconfirmed assumption presented as settled.** Copilot decided
   that a CANCELLED appointment can be rescheduled back to BOOKED. This
   was never confirmed by any requirement, and could reintroduce a
   duplicate-booking conflict (FR-05) if a cancelled slot is silently
   reopened.

5. **No unnecessary inheritance or invented dependencies.** Unlike the
   Tutorial's bad example, this output correctly avoided PatientRecord
   inheritance, SQL calls, and a NotificationManager dependency, in line
   with the explicit constraints given in the prompt.

6. **Incomplete error handling.** ValueError is raised for some illegal
   transitions (completed to cancelled, completed to modified), but
   nothing prevents cancelling an appointment that is already cancelled -
   the same missing invariant identified as the fifth design problem in
   the Tutorial's AI Code Critique.

## Part F - Manual Behaviour Checks

Tested the generated Appointment class with the following cases:

1. Valid appointment creation: Appointment("A001", "P001", "D001",
   datetime(2024, 7, 20, 10, 0)) - created successfully with status
   BOOKED.

2. Cancel a scheduled appointment: a.cancel() correctly changed status
   from BOOKED to CANCELLED.

3. Attempt an illegal repeated transition: calling a.cancel() a second
   time did not raise any error - the status remained CANCELLED with no
   exception. This confirms the missing invariant identified in Part E:
   cancel() only checks for COMPLETED status, not for an already-CANCELLED
   status.

4. Invalid input: Appointment("A002", "", "D001", "not-a-date") was
   accepted with no error at all, despite an empty patient_id and a
   plain string instead of a real datetime for time_slot. This shows
   that the type hints in the dataclass are not enforced at runtime -
   they are documentation only, not actual validation.

These results confirm two of the design problems flagged during Part E's
review: missing validation on repeated status transitions, and no input
validation on object creation.

## Part G - Refactor

Refactored the AI-generated Appointment class to fix the issues found
during Part F testing and simplify it to match the approved design:

1. Replaced the dataclass with a regular class using __init__, adding
   input validation (empty patient_id/practitioner_id, and a check that
   time_slot is an actual datetime object), matching the validation
   pattern already used in Patient and Practitioner.

2. Fixed the missing invariant in cancel() by adding a check for an
   already-CANCELLED status, closing the silent re-cancellation bug found
   in Part F.

3. Merged reschedule() and change_practitioner() into a single update()
   method, matching the approved UML, which only specified one update
   operation, not two separate ones.

4. Removed mark_completed(), since no requirement or approved UML element
   supported an actively-set "completed" status - this was unsupported
   scope invented by the AI.

Retested after refactoring:
- Created: AppointmentStatus.BOOKED
- After first cancel: AppointmentStatus.CANCELLED
- Second cancel attempt: correctly raised "Appointment is already
  cancelled."
- Invalid input (empty patient_id, non-datetime time_slot): correctly
  raised "Patient ID cannot be empty."

Both issues identified in Part F are now resolved.

## 1. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
| --- | --- | --- | --- |
| Patient class | Patient | Yes | patient_id, name, validated in __init__ |
| Practitioner class | Practitioner | Yes | practitioner_id, name, specialty, validated |
| Appointment class | Appointment | Yes | Refactored from AI version to add validation |
| Appointment.cancel() | cancel() | Yes | Now checks both COMPLETED and CANCELLED states |
| Appointment.update() | update() | Yes | Merged from two AI-invented methods into one |
| AppointmentStatus (status attribute) | AppointmentStatus enum | Yes | Added by AI, accepted as-is |
| Patient-Appointment association | patient_id reference | Partial | Currently stores ID string, not full object reference |
| Practitioner-Appointment association | practitioner_id reference | Partial | Same gap as above |

## 2. Domain Invariants

| Class | Invariant / rule | How protected |
| --- | --- | --- |
| Patient | name cannot be empty | ValueError in __init__ |
| Practitioner | name cannot be empty | ValueError in __init__ |
| Appointment | patient_id and practitioner_id cannot be empty | ValueError in __init__ |
| Appointment | time_slot must be a real datetime | ValueError in __init__ |
| Appointment | cannot cancel an already-cancelled appointment | ValueError in cancel() |
| Appointment | cannot cancel or modify a completed appointment | ValueError in cancel()/update() |

## 3. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
| --- | --- | --- |
| Appointment - Patient | Association | An appointment references a patient but is not a type of patient; has-a, not is-a |
| Appointment - Practitioner | Association | Same reasoning - an appointment references a practitioner, it does not inherit from it |
| Doctor - Practitioner (hypothetical) | Inheritance | A Doctor IS a type of Practitioner - a specialization of the same concept, so is-a applies |
| Clinic - Appointment | Association | A clinic may track appointments, but does not need to fully own or control their lifecycle |

## 4. AI Pair-Programming Record

| AI contribution | Conforms? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
| AppointmentStatus enum | Yes | Accepted | Matches UML's status attribute, keeps values controlled | Used directly in refactored code |
| Appointment as a dataclass with public fields | No | Rejected | Public status mutation bypasses transition rules | Confirmed via testing before refactor |
| reschedule() and change_practitioner() as separate methods | No | Modified | UML only specifies one update() operation | Merged into a single update() method |
| mark_completed() method | No | Rejected | No requirement or UML element supports this | Removed entirely |
| No check for re-cancelling an already-cancelled appointment | No | Modified | Missing invariant allowed a silent, incorrect state change | Added explicit check; confirmed via Part F retest |
| No validation on constructor inputs | No | Modified | Type hints are not enforced at runtime | Added explicit validation; confirmed via Part F retest |
| Avoided database, UI, notification, and service dependencies | Yes | Accepted | Correctly followed the explicit constraint list | Confirmed by reading the generated code |

## 5. Updated UML

The implementation revealed one gap from the Week 6 UML: Appointment was
implemented using patient_id/practitioner_id string references rather than
holding actual Patient/Practitioner objects as originally modelled. This
was inherited from the AI-generated version and not corrected during
refactoring. This is noted here as a known deviation for future
correction, rather than a deliberate design change.

---

## Reflection
The missing input validation felt like the most important issue to me,
since patient details are the most critical part of booking an
appointment. If the system silently accepts an empty patient ID or an
invalid time, the appointment record becomes meaningless - there would be
no reliable way to know who the appointment actually belongs to. This
made fixing the validation gap in the constructor feel more important
than some of the other issues, like the extra methods Copilot invented.

The approved design clearly constrained what Copilot produced this week
compared to Week 6. In Week 6, I didn't tell Copilot to avoid suggesting
extra classes, so it freely proposed things like PatientManager and
NotificationManager. This week, the prompt explicitly said not to add
database, UI, notification, or service classes, and Copilot actually
respected that constraint - the generated Appointment class had none of
those problems. This showed me that being specific about what an AI tool
should not do is just as important as saying what it should do.

Reading the generated code on its own, it looked reasonable - it used
type hints, an enum, and had methods with docstrings explaining each
decision. But once I actually tested it, running cancel() twice and
passing invalid input, I found real problems that weren't obvious just
from reading: cancelling an already-cancelled appointment succeeded
silently instead of raising an error, and an empty patient ID and a
non-datetime value were both accepted without any error at all. This
taught me that code can look well-structured and still fail in practice,
and that testing is necessary to actually verify a design's correctness,
not just its appearance.