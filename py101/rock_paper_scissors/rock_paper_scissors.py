"""
Play Rock, Paper, Scissors, Lizard, Spock!
"""
import random


VALID_CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}
GAME_RULES = {
    'rock': {
        'beats': ['scissors', 'lizard'],
        'is_beaten_by': ['paper', 'spock']
    },
     'paper': {
        'beats': ['rock', 'spock'],
        'is_beaten_by': ['scissors', 'lizard']
    },
     'scissors': {
        'beats': ['paper', 'lizard'],
        'is_beaten_by': ['rock', 'spock']
    },
     'lizard': {
        'beats': ['paper', 'spock'],
        'is_beaten_by': ['rock', 'scissors']
    },
     'spock': {
        'beats': ['rock', 'scissors'],
        'is_beaten_by': ['lizard', 'paper']
    },
}
score = {
    'player': 0,
    'computer': 0,
}


def prompt(message):
    """
    Pretty print a message
    """
    print(f'==> {message}')


def get_user_choice():
    """
    Get the user's choice, limiting to only valid options
    """
    prompt('Choose one:')
    for abbr, choice in VALID_CHOICES.items():
        prompt(f'{abbr} for {choice}')
    choice = VALID_CHOICES.get(input())

    while choice is None:
        prompt("That's not a valid choice")
        choice = VALID_CHOICES.get(input())

    return choice


def update_score(player, computer):
    """
    Determine who won, and update the score appropriately
    """
    prompt(f'You chose {player}, computer chose {computer}')

    if computer in GAME_RULES[player]['beats']:
        score['player'] += 1
        prompt('You get a point.')
    elif computer in GAME_RULES[player]['is_beaten_by']:
        score['computer'] += 1
        prompt('Computer gets a point.')
    else:
        prompt("It's a tie!")

    prompt(f'The current score is you: {score['player']} computer: {score['computer']}')


def check_game_over():
    """
    Determine if the match is over, and if so, reset
    """
    if score['player'] == 3:
        prompt('You won! Best of 5. Congratulations.')
        reset_score()
    elif score['computer'] == 3:
        prompt('Computer won, best of 5. Better luck next time.')
        reset_score()


def reset_score():
    """
    Reset scores to 0
    """
    global score
    score = {
        'player': 0,
        'computer': 0,
    }


def ask_play_again():
    """
    Ask the user to play again, and validate their response
    """
    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('y') or answer.startswith('n'):
            break

        prompt("That's not a valid choice")

    return answer


def play_game():
    """
    Play a round of the game
    """
    user_choice = get_user_choice()
    computer_choice = random.choice(list(VALID_CHOICES.values()))
    update_score(user_choice, computer_choice)

    check_game_over()

    answer = ask_play_again()
    if answer.startswith('y'):
        play_game()


play_game()
