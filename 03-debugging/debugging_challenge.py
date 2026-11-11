
"""
ACTIVITY 3: Debugging Challenge

The program below is supposed to calculate statistics
about a student's study sessions.

Before asking AI for help:
1. Read the code carefully.
2. Predict what the output should be.
3. Run the program and compare the results.
4. Ask your AI assistant to explain each bug before fixing it.
5. Test your program again after making changes.

Challenge: Find and fix all the bugs!
"""

session_lengths = [25, 30, 15, 45, 60]

session_subjects = [
    "Programming",
    "Mathematics",
    "Physics",
    "Programming",
    "Mathematics"
]

total = 0
longest_session = 0
shortest_session = 0
programming_sessions = 0

for i in range(len(session_lengths)):

    length = session_lengths[i]
    subject = session_subjects[i]

    # Calculate total study time
    total = length

    # Find the longest session
    if length < longest_session:
        longest_session = length

    # Find the shortest session
    if length > shortest_session:
        shortest_session = length

    # Count programming sessions
    if subject == "Mathematics":
        programming_sessions += 1


average = total / len(session_lengths)

print("\n===== STUDY SESSION REPORT =====")

print("Number of sessions:", len(session_lengths))
print("Total study time:", total, "minutes")
print("Average session length:", average, "minutes")

print("Longest session:", longest_session, "minutes")
print("Shortest session:", shortest_session, "minutes")

print("Programming sessions:", programming_sessions)


# BONUS CHALLENGES:
# 1. What happens if session_lengths is empty?
# 2. What happens if session_subjects has fewer items?
# 3. How could you prevent invalid or negative session lengths?
# 4. How could you calculate the total time for each subject?
