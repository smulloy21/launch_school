# Algorithm

"""
For this step, use your analysis of the problem so far to write out a
high-level algorithm that solves the problem at an abstract level.
Avoid too much implementation detail at this stage.
"""

# For each string in the list, determine the number of adjacent consonants
#   - for each letter in the word, keep track of greatest number of adjacent
#     consonants, ignoring spaces
#   - input: a string
#   - output: an integer, the count of highest # of adjacent consonants
#   - examples:
#       print(count_max_adjacent_consonants('dddaa'))       # 3
#       print(count_max_adjacent_consonants('ccaa'))        # 2
#       print(count_max_adjacent_consonants('baa'))         # 0
#       print(count_max_adjacent_consonants('aa'))          # 0
#       print(count_max_adjacent_consonants('rstafgdjecc')) # 4
#   - algorithm:
#       - remove spaces from string
#       - initialize max_consonants_count to 0
#       - initialize adjacent_consonants to ''
#       - for each letter in the string
#           - if the letter is a consonant, add it to adjacent_consonants
#           - if the letter is a vowel
#               - if length of adjacent consonants is greater than 1 and is greater than max_consonants_count
#                   - set max_consonants_count to length of adjacent consonants
#               - reset adjacent_consonants to ''
#       - return the max_consonants_count
# Sort the strings in the list by number of adjacent consonants, highest to fewest
# Return the sorted list
