print('Welcome to Calculator!')

print("What's the first number?")
number1 = int(input())

print("What's the second number?")
number2 = int(input())

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

if operation == '1':
    output = number1 + number2
elif operation == '2':
    output = number1 - number2
elif operation == '3':
    output = number1 * number2
elif operation == '4':
    output = number1 / number2

print(f"The result is: {output}")
