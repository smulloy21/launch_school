"""
A simple calculator for monthly mortgage payments
"""
import json
import math


with open('messages.json', 'r', encoding='utf-8') as file:
    MESSAGES = json.load(file)


def prompt(message, lang='en', context=None):
    """
    Pretty print the message in the right language, defaulting to English
    """
    if context is None:
        context = {}

    print(f'🏠 {MESSAGES[lang][message]}'.format(**context))


def get_valid_input(error_message):
    """
    Request input, validate with numeric conversion
    """
    while True:
        user_input = input()
        try:
            number = float(user_input)
        except ValueError:
            prompt(error_message)
        else:
            if not math.isfinite(number) or math.isnan(number):
                prompt(error_message)
            else:
                break
    return number


def get_loan_amount():
    """
    Get loan amount, convert to int
    """
    prompt('loan_amount')
    valid_loan_amount = get_valid_input('invalid_loan_amount')
    return valid_loan_amount


def get_monthly_interest():
    """
    Get APR, convert to monthly interest
    """
    prompt('apr')
    valid_apr = get_valid_input('invalid_apr')
    return valid_apr / 100 / 12


def get_duration():
    """
    Get duration in years, convert to months
    """
    prompt('duration')
    valid_duration = get_valid_input('invalid_duration')
    return valid_duration * 12


def calculate_monthly_payment(loan_amount, monthly_interest, duration_in_months):
    """
    Calculate the monthly payment, accounting for 0% APR
    """
    try:
        monthly_payment = loan_amount * (
            monthly_interest /
            (1 - (1 + monthly_interest) ** (-duration_in_months))
        )
    except ZeroDivisionError: # 0% interest
        monthly_payment = loan_amount / duration_in_months

    return monthly_payment


def calculate_again():
    """
    Ask the user if they want to calculate again
    """
    while True:
        prompt('continue')
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt('invalid')

    return answer


def calculate_mortgage():
    """
    Calculate monthly payment for a mortgage loan
    """
    prompt('welcome')
    loan_amount = get_loan_amount()
    monthly_interest = get_monthly_interest()
    duration_in_months = get_duration()
    monthly_payment = calculate_monthly_payment(loan_amount,
                                                monthly_interest,
                                                duration_in_months)

    prompt('result', context={"monthly_payment": monthly_payment})
    answer = calculate_again()
    if answer.startswith('y'):
        calculate_mortgage()


calculate_mortgage()
