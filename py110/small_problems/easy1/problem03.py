# Write another function that returns True if the string passed as an
# argument is a palindrome, or False otherwise. This time, however,
# your function should be case-insensitive, and should ignore all
# non-alphanumeric characters. If you wish, you may simplify things by
# calling the is_palindrome function you wrote in the previous exercise.

'''
P
input: a string
output: True or False
rules:
    explict:
        - return True if the string is a palindrome, otherwise False
        - the check should be case-insensitive
        - the check should ignore non-alphanumeric characters
    implicit:
        - do not worry about an empty string, ßor non-string inputs
E
behave as expected
D/A
- take the string, use a list comprehension to casefold it and strip any non-alphanumeric characters
- compare if the string is equal to its reverse

'''

def is_real_palindrome(string):
    string = [char.casefold() for char in string if char.isalnum()]
    return string == string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True
