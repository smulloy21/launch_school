# Write a function that takes a string as an argument and returns True
# if all parentheses in the string are properly balanced, False
# otherwise. To be properly balanced, parentheses must occur in
# matching '(' and ')' pairs.

'''
P
input: a string, with some amount of parentheses
output: True or False, of whether all parentheses are balanced
rules:
    explicit:
        - to be balanced, parentheses must occur in '(' and ')' pairs

E

D

A
- iterate over the characters in the string
- for each (, remove the leftmost ) starting at the current index
- if you cannot, return false
- if you can, return whether any ) are remaining or not (False if there are, True if not)
'''


def is_balanced(string):
    for i, char in enumerate(string):
        if char == '(':
            index = string.find(')', i)
            if index > 0:
                string = string[:index] + string[index + 1:]
            else:
                return False
    return not ')' in string



print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
