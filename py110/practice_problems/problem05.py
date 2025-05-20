# Create a function that takes a string argument and returns the character
# that occurs most often in the string. If there are multiple characters with
# the same greatest frequency, return the one that appears first in the
# string. When counting characters, consider uppercase and lowercase versions
# to be the same.

"""
P
input: a string
output: the character, lowercase, that occurs most often in the string (if tied, the first occuing character)
rules:
    - output is always lowercase, and case should be ignored


E

D

A
- lowercase the string
- dict comprehension for all characters and their counts
- get the lowest count, if tied, get the character whose index is first in the string

"""

def most_common_char(string):
    string = string.lower()
    letter_count = {char: string.count(char) for char in string}
    return max(letter_count, key=letter_count.get)


# Examples
print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')
# The above tests should each print True.
