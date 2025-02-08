# Write a function that takes a short line of text and prints it within
# a box.

def print_in_box(message):
    end_line = f'+-{'-' * len(message)}-+'
    empty_line = f'| {' ' * len(message)} |'

    print(end_line)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(end_line)


print_in_box('To boldly go where no one has gone before.')

# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

print_in_box('')

# +--+
# |  |
# |  |
# |  |
# +--+
