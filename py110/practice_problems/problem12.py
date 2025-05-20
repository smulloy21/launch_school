# Create a function that takes a string as an argument and returns True if the
# string is a pangram, False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least
# once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is
# a pangram since it uses every letter at least once. Note that case is
# irrelevant.

"""
P
input: a string
output: True or False, whether the input string in a pangram
rules:
- a pangram is a sentence that uses every letter of the alphabet at least once

E

D

A
high level:
- remove all non-alpha characters and casefold the string
- return whether the length of the set of all characters is 26

"""

ALPHABET_LENGTH = 26

def is_pangram(string):
    s = ''.join([char.casefold() for char in string if char.isalpha()])
    return len(set(s)) == ALPHABET_LENGTH


# Examples
print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)
# The above tests should each print True.
