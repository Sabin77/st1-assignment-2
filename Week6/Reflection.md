# Reflection

The hardest decision this week was figuring out where to draw the line
between "Copilot's suggestion sounds reasonable" and "Copilot's suggestion
is actually needed." When it proposed PatientManager and PractitionerManager,
its reasoning looked solid at first glance - it cited real requirement IDs
like FR-01 and FR-02. But when I actually read the justification closely, it
was really just saying "this requirement needs some logic," not "this
requirement needs its own class." That distinction wasn't obvious to me
right away, and it took re-reading the response a couple of times before I
noticed the gap.

That's basically where I think AI over-designed. It defaulted to a familiar
Manager/Controller/Service pattern for almost everything, even when a
requirement could be handled by the class itself without extra wrapping. It
felt like it was reaching for a "proper" software architecture template
rather than actually asking whether SmartCare, as a small, simple system,
needed that much structure.

What did hold up well was AppointmentManager and ReportService, and that's
because the justification for those was genuinely different - FR-05 needs
to check for conflicts across multiple appointments, not just one, and FR-12
needs to look across a date range. Those aren't things a single Appointment
object can reasonably do by itself, so keeping some form of that logic
separate made sense.

In the end, the evidence that mattered most was whether a suggestion solved
something a single object genuinely couldn't do alone. If it could, I
rejected the extra class. If it couldn't, I kept the idea but tried to keep
it as small and simple as possible instead of accepting AI's more elaborate
version.