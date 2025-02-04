"""
A simple calculator for monthly mortgage payments
"""
import json


with open('messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)


def prompt(message, lang='en', context={}):
    """
    Pretty print the message in the right language, defaulting to English
    """
    print(f'🏠 {MESSAGES[lang][message]}'.format(**context))


def get_valid_input(error_message):
    """
    Request input, validate with numeric conversion
    """
    while True:
        user_input = input()
        try:
            float(user_input)
        except ValueError:
            prompt(error_message)
        else:
            break
    return user_input


def get_loan_amount():
    """
    Get loan amount, convert to int
    """
    prompt('loan_amount')
    valid_loan_amount = get_valid_input('invalid_loan_amount')
    return int(valid_loan_amount)



def get_monthly_interest():
    """
    Get APR, convert to monthly interest
    """
    prompt('apr')
    valid_apr = get_valid_input('invalid_apr')
    return float(valid_apr) / 100 / 12


def get_duration():
    """
    Get duration in years, convert to months
    """
    prompt('duration')
    valid_duration = get_valid_input('invalid_duration')
    return float(valid_duration) * 12


def calculate_mortgage():
    """
    Calculate monthly payment for a mortgage loan
    """
    prompt('welcome')
    loan_amount = get_loan_amount()
    monthly_interest = get_monthly_interest()
    duration_in_months = get_duration()
    try:
        monthly_payment = loan_amount * (
            monthly_interest /
            (1 - (1 + monthly_interest) ** (-duration_in_months))
        )
    except ZeroDivisionError: # 0% interest
        monthly_payment = loan_amount / duration_in_months
    prompt('result', context={"monthly_payment": monthly_payment})


calculate_mortgage()
