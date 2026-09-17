# My Reflection
Before using AI, I built a Python file that stored appointments using a list
of dictionaries and two functions, book_appointment() and
display_appointments(). I tested it by running the code and tried to add an
appointment but it had limitations like, unable to store more than a couple
of hardcoded appointments, no validation on practitioner name or time, no
check for double booking, etc.

When I asked Copilot to act as a tutor, it explained how the code works and
what its limitations are. It also asked me two questions: one about what
Python data structure is used to store multiple appointments, and why it is
suitable, and one about what happens inside book_appointment(). Answering
these made me realize how the dictionaries and functions work.

When I asked Copilot to generate its own version of the function, it assumed
that all input would always be valid. It didn't include any check for empty
values.

I tested both my version and the AI's version with the same four inputs: a
normal appointment, a blank patient name, a duplicate appointment, and None
values. I found that my version raised an error on blank/None input, while
the AI's version silently accepted it.

Even though AI generated a working function, I still had to decide which fix
mattered, test both versions myself, judge which one was actually better for
a real receptionist to use, and understand the code well enough to explain
it.