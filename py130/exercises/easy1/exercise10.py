def generator():
    while True:
        string = input('Enter anything but stop: ')
        if string == 'stop':
            break
        yield string


for user_input in generator():
    print(user_input)
