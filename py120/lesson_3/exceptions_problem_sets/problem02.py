num1 = input('Enter a number: ')
num2 = input('Enter another number: ')

try:
    result = float(num1) / float(num2)
except ZeroDivisionError:
    print('Whoops, zero division error raised!')
except ValueError:
    print('Invalid number entered.')
else:
    print(f'The result is: {result}')
finally:
    print('End of the program')
