# Examples and test cases

"""
You are provided with the following test cases for this problem.

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']

Regarding your initial mental model and questions from Step 1, make
some notes about the test cases. Do the test cases confirm or refute
different elements of your original analysis and mental model? Do they
answer any of the questions that you had, or do they perhaps raise
further questions?
"""

# rules:
#   implicit:
#       - strings must have two adjacent consonants to count
#       - sort order is from most consonants adacent to fewest
#       - case is not relevant
#       - don't worry about empty strings (for now)
