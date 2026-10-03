## Tutorial Activity 1 - Where Does This Belong?

| Responsibility | Layer | Reason |
| --- | --- | --- |
| Read menu input | Presentation | User interaction, not business logic |
| Check appointment status transition | Domain | Business rule belonging to Appointment itself |
| Coordinate booking use case | Service | Orchestrates multiple steps across layers |
| Execute SQLite INSERT | Persistence | Raw data storage operation |
| Format confirmation message | Presentation | Output formatting for the user |
| Find appointment by ID | Repository | Data retrieval operation |

## Tutorial Activity 2 - Architecture Smell Hunt

A file mixing input(), SQL, conflict rules, printing and validation has these problems:
1. No separation of concerns - everything lives in one file
2. Business rules (conflict checking) are mixed with persistence (SQL)
3. Presentation code (input/print) is mixed with domain logic
4. Hard to test - can't test conflict logic without a real database
5. Hard to change - swapping databases means touching UI and business code too

Proposed layers: input/print -> Presentation; conflict rules -> Domain/Service; SQL -> Persistence.

## Tutorial Activity 3 - SOLID Without Overengineering

- ClinicManager handling every use case violates Single Responsibility Principle (SRP).
- AppointmentService importing sqlite3 directly violates Dependency Inversion Principle (DIP) - it should depend on an abstraction, not a concrete library.
- A 20-method interface when a client needs 2 violates Interface Segregation Principle (ISP).
- Not every class needs an interface - only introduce one where multiple implementations are genuinely expected (e.g. Repository).

## Tutorial Activity 4 - AI Architecture Critique

If AI proposed microservices, an event bus, six interfaces, and a DI framework:
- Reject: microservices and event bus - wildly disproportionate for a small single-clinic app
- Defer: DI framework - plain constructor injection (already used here) is sufficient
- Keep: one repository interface, since it's already justified by the need to swap storage implementations

## Current Architecture Problems

| Problem | Evidence | Impact | Refactoring |
| --- | --- | --- | --- |
| Conflict policy lived in Repository | has_conflict() in AppointmentRepository | Mixed persistence with business rules | Moved conflict check into AppointmentService |
| Repository leaked internal list | get_all() returned self.appointments directly | Callers could mutate/corrupt stored data | Changed to return list(self.appointments) |
| update() bypassed constructor validation | new_time accepted without type check | Invalid data could corrupt an existing object | Added isinstance check in update() |
| Service dependency was implicit | def __init__(self, repository) with no type hint | Unclear what repository must support | Added AppointmentRepository type hint |
| Cancelled appointments blocked rebooking | has_conflict() ignored status | Freed slots stayed falsely blocked | Conflict check now excludes CANCELLED status |

## Layer Responsibilities

| Layer | Responsibilities | Must not contain |
| --- | --- | --- |
| Presentation | Input/output, formatting messages | Business rules, data access |
| Service | Coordinating workflow, cross-object rules (conflict checking) | Direct database/storage code |
| Domain | Entity state, lifecycle rules, validation | Persistence or UI code |
| Repository | Storing/retrieving data | Business/scheduling policy |
| Persistence | Concrete storage implementation | Business rules |

## SOLID Review

| Principle | Relevant? | Evidence | Decision |
| --- | --- | --- | --- |
| SRP | Yes | has_conflict() mixed policy into Repository | Moved to Service |
| OCP | Yes | New repository implementations can replace InMemory without changing Service | Kept as-is, no change needed |
| LSP | Minor | Base repository contract was informal | Addressed via type hint |
| ISP | No | Repository only has 3-4 small methods | No interface splitting needed |
| DIP | Yes | Service depended on repository without explicit type | Added AppointmentRepository type hint |

## AI Architecture Review

| AI suggestion | Observed problem? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
| Move has_conflict() out of Repository into Service | Yes | Accepted | Scheduling policy is a business rule, not persistence | Retested booking/conflict - still works correctly |
| get_all() should return a copy, not internal list | Yes | Accepted | Prevented external code from corrupting stored data | Confirmed via code review |
| update() should validate new_time/new_practitioner_id | Yes | Accepted | Constructor validated but update() did not - confirmed in testing | Tested update() with invalid input - now correctly raises ValueError |
| Conflict check should ignore CANCELLED appointments | Yes | Accepted (business rule confirmed) | Matches FR-05's intent - only active bookings should block a slot | Tested: rebooking after cancellation succeeded |
| Add type hint to Service constructor | No (style only) | Accepted | Low-risk clarity improvement, no behaviour change | Code review only |
| Add Patient/Practitioner lookup before booking | No | Rejected (deferred) | No current requirement demands this; AI itself cautioned against adding infrastructure without justification | N/A |
| Split Repository into Reader/Writer/ConflictChecker interfaces | No | Rejected | AI itself called this "needless complexity" for this system's size | N/A |

