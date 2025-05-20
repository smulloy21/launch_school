# Create a function that takes a non-empty string as an argument. The string
# consists entirely of lowercase alphabetic characters. The function should
# return the length of the longest vowel substring. The vowels of interest are
# "a", "e", "i", "o", and "u".

"""
P
input: a non-empty string of lowercase alphabetic characters
output: the length of the longest vowel substring
rules:
- vowels of interest are: 'a' 'e' 'i' 'o' and 'u'

E

D

A
- initialize a counter for longest vowel substring, set equal to 0
- initialize a counter for current vowels substring, set equal to 0
- for each character in the string, if in the string of `vowels`, add 1 to the current vowels substring,
else set current vowels substring to 0
-- if the current vowels substring is longer than longest vowel substring, set longest vowel substring to current vowel substring
- return longest vowel substring

"""

def longest_vowel_substring(string):
    longest_vowels, current_vowels = 0, 0
    for char in string:
        if char in 'aeiou':
            current_vowels += 1
        else:
            current_vowels = 0
        if current_vowels > longest_vowels:
            longest_vowels = current_vowels

    return longest_vowels


# Examples
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)
# The above tests should each print True.
