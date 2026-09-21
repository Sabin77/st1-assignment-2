# Reflection

In checking my requirements with AI, I found one I had missed.
My requirement on searching patients (FR-02) didn't specify that the search
should be case-insensitive and support full names. Instead, it specified
"search by name or ID." But my own user story (US-01) already contained a
case-insensitive partial match. Thus, I learned that the acceptance criteria
of a requirement must contain everything explicitly, rather than implying it
from another part of the document.

The other suggestion from AI was to clarify how practitioners will be
authenticated. That was a fair point, but I concluded that such clarification
is unnecessary at this stage, as our brief describes a simple appointment
and record management system without any user accounts or any sort of login
security involved. Adding such a requirement now would mean going beyond
what our client has actually asked for.

Following the review, I have added more detail to FR-02 and extended it to
support full or partial name matches and case-insensitivity. I did that,
as this modification is based on evidence available in my own document.

Requirements must always have evidence, as even AI and human intuition may
produce suggestions of additional features or clarifications that sound
reasonable but were never actually requested by the client. Without tracing
every requirement back to the brief or a stakeholder's stated need, a
project risks building features nobody asked for while missing what was
genuinely needed. Evidence keeps requirements accountable to the real
problem being solved.