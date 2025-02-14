# Examples and test cases

"""
You are provided with the following test cases for this problem.

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

Regarding your initial mental model and questions from Step 1, make
some notes about the test cases. Do the test cases confirm or refute
different elements of your original analysis and mental model? Do they
answer any of the questions that you had, or do they perhaps raise
further questions?
"""

# rules:
#   implicit:
#       - A layer should have the minimum needed number of blocks
#       - There are not always leftover blocks
