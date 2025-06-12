# Create a function named print_message that requires a keyword-only argument
# (message) and an optional keyword-only argument (level) with a default value
# of "INFO". The function should print out the message prefixed with the
# level. The function shouldn't accept any positional arguments.


def print_message(*, message, level='INFO'):
    print(f'[{level}] {message}')

print_message(message="This is a test message.", level="WARNING")
# [WARNING] This is a test message.

print_message(message="This is an informational message.")
# [INFO] This is an informational message.
