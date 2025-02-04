import json

with open('calculator_messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]

prompt(messages("welcome_prompt"))

while True:
    prompt(messages("number1_prompt"))
    number1 = input()

    while invalid_number(number1):
        prompt(messages("invalid_number_prompt"))
        number1 = input()

    prompt(messages("number2_prompt"))
    number2 = input()

    while invalid_number(number2):
        prompt(messages("invalid_number_prompt"))
        number2 = input()

    prompt(messages("operation_prompt"))
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(messages("invalid_operation_prompt"))
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt(messages("result_prompt").format(output=output))
    prompt(messages("repeat_prompt"))
    continue_answer = input()
    if continue_answer and continue_answer[0].lower() != 'y':
        break
