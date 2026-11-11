"""
ACTIVITY 3: Debugging challenge

The program below is supposed to calculate the average session length.
It contains an intentional logic bug.

Before asking AI for help:
1. Read the code.
2. Predict what the output should be.
3. Run the program and compare the result.
4. Ask your AI assistant to explain the bug before asking for a fix.
"""

session_lengths = [25, 30, 15]

total = 0

for length in session_lengths:
    total = length  # BUG: this replaces total instead of adding to it

average = total / len(session_lengths)

print("Average session length:", average, "minutes")

# BONUS:
# What would happen if session_lengths were an empty list?
# Ask your AI assistant how to handle that case safely.
