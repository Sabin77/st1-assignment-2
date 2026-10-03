# Reflection

One AI suggestion I accepted was moving the conflict-checking logic out of
the Repository and into the Service. This made sense because checking
whether a practitioner is already booked is a business rule, not a storage
operation - the Repository should only answer what data exists, not decide
what is valid.

One suggestion I modified rather than accepted outright was excluding
cancelled appointments from conflict checks. The underlying fix was correct,
but I treated it as a business-rule decision that needed to match FR-05's
intent, rather than blindly applying a code change - testing afterward
confirmed rebooking a cancelled slot now works correctly.

One suggestion I rejected was adding Patient and Practitioner lookups before
booking. Copilot itself pointed out that this would add infrastructure
without a confirmed requirement demanding it, and I agreed - the current
system only needs appointment scheduling by ID, so adding this now would be
unjustified complexity.

Overall, this AI review stayed disciplined and avoided proposing
microservices or frameworks, which made it easier to trust its suggestions
and focus on the handful that were genuinely justified by the existing code.