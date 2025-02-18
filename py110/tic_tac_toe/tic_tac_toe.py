import os
import random


INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
PLAYER = 'Player'
COMPUTER = 'Computer'
ROUNDS = 3
WINNING_LINES = [
    ['A1', 'A2', 'A3'], ['A4', 'A5', 'A6'], ['A7', 'A8', 'A9'],  # A rows
    ['A1', 'A4', 'A7'], ['A2', 'A5', 'A8'], ['A3', 'A6', 'A9'],  # A columns
    ['A1', 'A5', 'A9'], ['A3', 'A5', 'A7'],                      # A diagonals
    ['B1', 'B2', 'B3'], ['B4', 'B5', 'B6'], ['B7', 'B8', 'B9'],  # B rows
    ['B1', 'B4', 'B7'], ['B2', 'B5', 'B8'], ['B3', 'B6', 'B9'],  # B columns
    ['B1', 'B5', 'B9'], ['B3', 'B5', 'B7'],                      # B diagonals
    ['C1', 'C2', 'C3'], ['C4', 'C5', 'C6'], ['C7', 'C8', 'C9'],  # C rows
    ['C1', 'C4', 'C7'], ['C2', 'C5', 'C8'], ['C3', 'C6', 'C9'],  # C columns
    ['C1', 'C5', 'C9'], ['C3', 'C5', 'C7'],                      # C diagonals
    ['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'],  # verticals
    ['A4', 'B4', 'C4'], ['A5', 'B5', 'C5'], ['A6', 'B6', 'C6'],  # verticals
    ['A7', 'B7', 'C7'], ['A8', 'B8', 'C8'], ['A9', 'B9', 'C9'],  # verticals
    ['A1', 'B2', 'C3'], ['A3', 'B2', 'C1'],                      # vertical diagonals
    ['A4', 'B5', 'C6'], ['A6', 'B5', 'C4'],                      # vertical diagonals
    ['A7', 'B8', 'C9'], ['A9', 'B8', 'C7'],                      # vertical diagonals
    ['A1', 'B4', 'C7'], ['A7', 'B4', 'C1'],                      # vertical diagonals
    ['A2', 'B5', 'C8'], ['A8', 'B5', 'C2'],                      # vertical diagonals
    ['A3', 'B6', 'C9'], ['A9', 'B6', 'C3'],                      # vertical diagonals
    ['A1', 'B5', 'C9'], ['A9', 'B5', 'C1'],                      # cross diagonals
    ['A3', 'B5', 'C7'], ['A7', 'B5', 'C3'],                      # cross diagonals
]
CENTER_SQUARE = 'B5'


def prompt(message):
    print(f'==> {message}')


def display_board(board, score):
    os.system('clear')

    prompt("Welcome to 3D Tic Tac Toe!")
    prompt("Board A is atop board B which is atop board C.")
    prompt(f"You are {PLAYER_MARKER}. Computer is {COMPUTER_MARKER}.")
    print()
    print('     |     |             |     |             |     |')
    print(f"  {board['A1']}  |  {board['A2']}  |  {board['A3']}     "
          f"  {board['B1']}  |  {board['B2']}  |  {board['B3']}     "
          f"  {board['C1']}  |  {board['C2']}  |  {board['C3']}")
    print('     |     |             |     |             |     |')
    print('-----+-----+-----   -----+-----+-----   -----+-----+-----')
    print('     |     |             |     |             |     |')
    print(f"  {board['A4']}  |  {board['A5']}  |  {board['A6']}     "
          f"  {board['B4']}  |  {board['B5']}  |  {board['B6']}     "
          f"  {board['C4']}  |  {board['C5']}  |  {board['C6']}")
    print('     |     |             |     |             |     |')
    print('-----+-----+-----   -----+-----+-----   -----+-----+-----')
    print('     |     |             |     |             |     |')
    print(f"  {board['A7']}  |  {board['A8']}  |  {board['A9']}     "
          f"  {board['B7']}  |  {board['B8']}  |  {board['B9']}     "
          f"  {board['C7']}  |  {board['C8']}  |  {board['C9']}")
    print('     |     |             |     |             |     |')
    print()
    print('     Board A             Board B             Board C')
    print()
    prompt(f'Score is Player: {score[PLAYER]} Computer: {score[COMPUTER]}')


def initialize_board():
    full_board = {}
    for board in 'ABC':
        for num in range(1,10):
            square = f'{board}{num}'
            full_board[square] = INITIAL_MARKER
    return full_board


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def join_or(options, seperator=', ', final_joiner='or'):
    if not options:
        return ''
    if len(options) == 1:
        return options[0]
    if len(options) == 2:
        return f'{options[0]} {final_joiner} {options[1]}'

    return f'{seperator.join(options[0:-1])}{seperator}{final_joiner} {options[-1]}'


def player_chooses_square(board):
    while True:
        valid_choices = empty_squares(board)
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip().upper()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[square] = PLAYER_MARKER


def computer_chooses_square(board):
    square = None

    # offense
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break

    # defense
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, PLAYER_MARKER)
            if square:
                break

    # choose center
    if not square:
        if board[CENTER_SQUARE] == INITIAL_MARKER:
            square = CENTER_SQUARE

    # random
    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None


def board_full(board):
    return len(empty_squares(board)) == 0


def someone_won(board):
    return bool(detect_winner(board))


def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == PLAYER_MARKER
               and board[sq2] == PLAYER_MARKER
               and board[sq3] == PLAYER_MARKER):
            return PLAYER
        if (board[sq1] == COMPUTER_MARKER
                  and board[sq2] == COMPUTER_MARKER
                  and board[sq3] == COMPUTER_MARKER):
            return COMPUTER

    return None


def choose_start_player():
    while True:
        prompt('Choose who will begin, p for player, c for computer:')
        start_player = input().strip().lower()

        if start_player in ('p', 'player'):
            return PLAYER
        if start_player in ('c', 'computer'):
            return COMPUTER

        prompt('That\'s not a valid choice.')


def choose_square(board, current_player):
    if current_player == PLAYER:
        player_chooses_square(board)
    else:
        computer_chooses_square(board)


def alternate_player(current_player):
    if current_player == PLAYER:
        return COMPUTER

    return PLAYER


def new_score():
    return {PLAYER: 0, COMPUTER: 0}


def play_tic_tac_toe():
    score = new_score()

    while True:
        # play a round
        board = initialize_board()
        display_board(board, score)
        current_player = choose_start_player()

        while True:
            # take a turn
            display_board(board, score)

            choose_square(board, current_player)
            if someone_won(board) or board_full(board):
                break

            current_player = alternate_player(current_player)

        if someone_won(board):
            winner = detect_winner(board)
            score[winner] += 1
            if score[winner] == ROUNDS:
                display_board(board, score)
                prompt(f"{winner} won the game and the match!")
                score = new_score()
            else:
                display_board(board, score)
                prompt(f'{winner} won the game! Continue for best of 5.')
        else:
            display_board(board, score)
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().strip().lower()

        if answer not in ('y', 'yes'):
            break

    prompt('Thanks for playing!')


play_tic_tac_toe()
