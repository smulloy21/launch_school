# Write a function that returns True if the string passed as an
# argument is a palindrome, False otherwise. A palindrome reads the
# same forwards and backwards. For this problem, the case matters and
# all characters matter.

'''
P
input: a string
output: True if the string is a palindrome, otherwise False
rules:
    explicit:
        - a palindrome reads the same forwards and backwards
        - case matters and all characters matter
    implicit:
        - don't need to handle an empty string

E
all behave as expected

D/A
return whether the string is equal to the string in reverse
'''

def is_palindrome(string):
    return string == string[::-1]


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
