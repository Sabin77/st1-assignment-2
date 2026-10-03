# AI Usage Log - Week 8

## Prompt used with Copilot
Act as a software architecture reviewer. Review this small SmartCare Python
system against separation of concerns, cohesion, coupling and introductory
SOLID principles. Identify concrete layer violations and dependency risks.
Prefer the simplest refactoring that solves an observed problem. Do not
introduce frameworks, microservices or patterns unless current requirements
justify them.

[Pasted domain.py, appointment_repository.py, appointment_service.py, main.py]

## Summary of Copilot's response
Copilot identified 6 concrete issues: conflict policy misplaced in the
Repository, an implicit Service dependency contract, repository list
exposure, a bypassable update() invariant, a cancelled-appointment conflict
bug, and a disconnected Patient/Practitioner model. It explicitly declined
to recommend microservices, a DI framework, or interface splitting, citing
the system's small size, and stated: "refactor toward clearer
responsibilities, not patterns."

## My evaluation
I accepted five of Copilot's concrete fixes (conflict policy relocation,
list copy, update() validation, cancelled-appointment handling, and the
type hint) since each was verifiable and matched problems I could confirm
through testing. I rejected the Patient/Practitioner lookup suggestion and
the interface-splitting suggestion, both of which Copilot itself flagged as
unnecessary for this system's current requirements.