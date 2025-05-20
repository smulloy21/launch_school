# Create a function that takes two strings as arguments and returns True if
# some portion of the characters in the first string can be rearranged to
# match the characters in the second. Otherwise, the function should return
# False.

# You may assume that both string arguments only contain lowercase alphabetic
# characters. Neither string will be empty.

"""
P
input: two strings
output: True or False, whether the first string can be rearranged to create the second

E

D

A
high-level:
- create a character: count dict for each string
- for each letter in the second string, if the first dict has less than the necessary count
(the necessary count being the count in the second dict), return False, else continue
- return True

"""

def unscramble(string1, string2):
    dict1 = {char: string1.count(char) for char in string1}
    dict2 = {char: string2.count(char) for char in string2}
    for char in string2:
        if dict1.get(char, 0) < dict2[char]:
            return False
    return True

# Examples
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)
# The above tests should each print True.
