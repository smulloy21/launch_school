# Write a function that takes a string and returns a dictionary
# containing the following three properties:

# - the percentage of characters in the string that are lowercase
# letters
# - the percentage of characters that are uppercase letters
# - the percentage of characters that are neither

# All three percentages should be returned as strings whose numeric
# values lie between "0.00" and "100.00", respectively. Each value
# should be rounded to two decimal points.

# You may assume that the string will always contain at least one
# character.


'''
P
input: a string
output: a dictionary, containing the percent of chars that are lower, upper, and neither
rules:
    - all three percents should be strings between "0.00" and "100.00", rounded to 2 decimal points
    - string will always contain at least 1 character

E

D

A
- `total` = total length of the string
- `uppercase` = length of a list comprehension of all uppercase characters
- `lowercase` = length of a list comprehension of all lowercase characters
-  `neither` = length of a list comprehendion of all other characters in the string
- return a dict of the percent of each uppercase, lowercase, and neighter, converted to 2 decimal rounded string format
'''


def letter_percentages(string):
    total_chars = len(string)
    uppercase_chars = len([char for char in string if char.isupper()])
    lowercase_chars = len([char for char in string if char.islower()])
    neither_chars = len([char for char in string if not char.isalpha()])
    return {
        'lowercase': f'{lowercase_chars/total_chars * 100:.2f}',
        'uppercase': f'{uppercase_chars/total_chars * 100:.2f}',
        'neither': f'{neither_chars/total_chars * 100:.2f}'
    }


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
