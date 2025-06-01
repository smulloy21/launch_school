class NegativeNumberError(Exception):
    def __init__(self, message='Number cannot be negative!'):
        super().__init__(message)

num = float(input('Enter a number: '))

if num < 0:
    raise NegativeNumberError()
print(f'You entered: {num}')
