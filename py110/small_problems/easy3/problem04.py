# Write a function that takes a string, doubles every consonant in the
# string, and returns the result as a new string. The function should
# not double vowels ('a','e','i','o','u'), digits, punctuation, or
# whitespace.

# You may assume that only ASCII characters will be included in the
# argument.

'''
P
input: a string
output: the string with every consonant doubled
rules:
    explicit:
        - do not double anything except consonants
        - you can assume only ascii characters are in the string

E

D

A
- in a list comprehension, append every consonant twice (isalpha and not in vowels) otherwise
append each character once
- join the list into a string
'''

def double_consonants(string):
    vowels = ('a','e','i','o','u')
    return ''.join([char * 2 if char.isalpha() and char.casefold() not in vowels
                    else char for char in string])

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
