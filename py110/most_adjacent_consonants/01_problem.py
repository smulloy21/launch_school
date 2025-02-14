# Understand the problem

"""
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the highest number of
adjacent consonants a string contains and return the sorted list. If
two strings contain the same highest number of adjacent consonants,
they should retain their original order in relation to each other.
Consonants are considered adjacent if they are next to each other in
the same word or if there is a space between two consonants in adjacent
words.

Tasks
You are provided with the problem description above. Your tasks for
this step are:

- Make notes of your mental model for the problem, including:
-- inputs and outputs.
-- explicit and implicit rules.
- Write a list of clarifying questions for anything that isn't clear.
"""

# input: list of strings
# output: the list of string sorted by highest number of adjacent consonants
# rules:
#   explicit:
#       - consonants are adjacent if they are next to each other in the same
#         word, or there is a space between them in adjacent words
#       - if two strings contain the same highest number of adjacent
#         consonants, retain their original order
#       - the output should be the sorted list, not a new list
#   implicit:
#       - strings may have more than one word
# questions:
#       - is case important?
#       - what should we do with empty strings?
#       - what about punctionation? I'm assuming that it impedes adjacency
