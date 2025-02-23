# Write a program that solicits six (6) numbers from the user and
# prints a message that describes whether the sixth number appears
# among the first five.

# Example 1:
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.

# Example 2:
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

'''
P
input: 6 numbers via terminal input
output: a string describing whether the sixth number is among the previous 5
rules:
    explicit:
        - the user should be asked for 6 numbers and then told if the 6th number is
        among the previous 5
    implicit:
        - only need to handle valid integer responses from the user
E
D/A
Ask the user for six numbers. Store them in a list
and determine if the sixth number is in the list of the previous 5. Print the result
for the user to see.
'''

seen = []
for nth in ('1st', '2nd', '3rd', '4th', '5th'):
    num = input(f'Enter the {nth} number: ')
    seen.append(num)

last = input('Enter the last number: ')
if last in seen:
    print(f'{last} is in {','.join(seen)}.')
else:
    print(f'{last} isn\'t in {','.join(seen)}.')
