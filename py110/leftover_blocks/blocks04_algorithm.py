# Algorithm

"""
For this step, use your analysis of the problem so far to write out a
high-level algorithm that solves the problem at an abstract level.
Avoid too much implementation detail at this stage.
"""

# Initialize a list that is the number of blocks in each row
# While the sum of this list is less than the input, add new row
# Once the sum equals or exceeds the input, stop. If it exceeds, remove the final row
# The leftover blocks are the remainder of input - sum of list
