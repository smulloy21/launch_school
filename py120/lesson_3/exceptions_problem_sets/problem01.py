# Write a program that asks the user for two numbers and divides the first
# number by the second number. Handle any potential ZeroDivisionError or
# ValueError exceptions (there is no need to retry inputs in this problem).

num1 = input('Enter a number: ')
num2 = input('Enter another number: ')

try:
    result = float(num1) / float(num2)
    print(f'The result is: {result}')
except ZeroDivisionError:
    print('Whoops, zero division error raised!')
except ValueError:
    print('Invalid number entered.')
