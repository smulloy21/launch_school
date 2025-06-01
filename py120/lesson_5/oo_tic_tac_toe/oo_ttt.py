import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares['A1']}  |"
              f"  {self.squares['A2']}  |"
              f"  {self.squares['A3']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['A4']}  |"
              f"  {self.squares['A5']}  |"
              f"  {self.squares['A6']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['A7']}  |"
              f"  {self.squares['A8']}  |"
              f"  {self.squares['A9']}")
        print("     |     |")
        print()
        print('     Board A')
        print()
        print("     |     |")
        print(f"  {self.squares['B1']}  |"
              f"  {self.squares['B2']}  |"
              f"  {self.squares['B3']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['B4']}  |"
              f"  {self.squares['B5']}  |"
              f"  {self.squares['B6']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['B7']}  |"
              f"  {self.squares['B8']}  |"
              f"  {self.squares['B9']}")
        print("     |     |")
        print()
        print('     Board B')
        print()
        print("     |     |")
        print(f"  {self.squares['C1']}  |"
              f"  {self.squares['C2']}  |"
              f"  {self.squares['C3']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['C4']}  |"
              f"  {self.squares['C5']}  |"
              f"  {self.squares['C6']}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares['C7']}  |"
              f"  {self.squares['C8']}  |"
              f"  {self.squares['C9']}")
        print("     |     |")
        print()
        print('     Board C')
        print()

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def reset(self):
        self.squares = {f'{board}{key}': Square()
                        for board in ['A', 'B', 'C']
                        for key in range(1, 10)
        }

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def is_unused_square(self, key):
        return self.squares[key].is_unused()

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    MATCH_GOAL = 3
    POSSIBLE_WINNING_ROWS = (
        ('A1', 'A2', 'A3'),  # top row of board A
        ('A4', 'A5', 'A6'),  # center row of board A
        ('A7', 'A8', 'A9'),  # bottom row of board A
        ('A1', 'A4', 'A7'),  # left column of board A
        ('A2', 'A5', 'A8'),  # middle column of board A
        ('A3', 'A6', 'A9'),  # right column of board A
        ('A1', 'A5', 'A9'),  # diagonal: top-left to bottom-right A
        ('A3', 'A5', 'A7'),  # diagonal: top-right to bottom-left A
        ('B1', 'B2', 'B3'),  # top row of board B
        ('B4', 'B5', 'B6'),  # center row of board B
        ('B7', 'B8', 'B9'),  # bottom row of board B
        ('B1', 'B4', 'B7'),  # left column of board B
        ('B2', 'B5', 'B8'),  # middle column of board B
        ('B3', 'B6', 'B9'),  # right column of board B
        ('B1', 'B5', 'B9'),  # diagonal: top-left to bottom-right B
        ('B3', 'B5', 'B7'),  # diagonal: top-right to bottom-left B
        ('C1', 'C2', 'C3'),  # top row of board C
        ('C4', 'C5', 'C6'),  # center row of board C
        ('C7', 'C8', 'C9'),  # bottom row of board C
        ('C1', 'C4', 'C7'),  # left column of board C
        ('C2', 'C5', 'C8'),  # middle column of board C
        ('C3', 'C6', 'C9'),  # right column of board C
        ('C1', 'C5', 'C9'),  # diagonal: top-left to bottom-right C
        ('C3', 'C5', 'C7'),  # diagonal: top-right to bottom-left C
        ('A1', 'B1', 'C1'),  # uprights
        ('A2', 'B2', 'C2'),  # uprights
        ('A3', 'B3', 'C3'),  # uprights
        ('A4', 'B4', 'C4'),  # uprights
        ('A5', 'B5', 'C5'),  # uprights
        ('A6', 'B6', 'C6'),  # uprights
        ('A7', 'B7', 'C7'),  # uprights
        ('A8', 'B8', 'C8'),  # uprights
        ('A9', 'B9', 'C9'),  # uprights
        ('A1', 'B2', 'C3'),  # upright diagonal
        ('A3', 'B2', 'C1'),  # upright diagonal
        ('A4', 'B5', 'C6'),  # upright diagonal
        ('A6', 'B5', 'C4'),  # upright diagonal
        ('A7', 'B8', 'C9'),  # upright diagonal
        ('A9', 'B8', 'C7'),  # upright diagonal
        ('A1', 'B4', 'C7'),  # upright diagonal
        ('A7', 'B4', 'C1'),  # upright diagonal
        ('A2', 'B5', 'C8'),  # upright diagonal
        ('A8', 'B5', 'C2'),  # upright diagonal
        ('A3', 'B6', 'C9'),  # upright diagonal
        ('A9', 'B6', 'C3'),  # upright diagonal
        ('A1', 'B5', 'C9'),  # cross diagonal
        ('A9', 'B5', 'C1'),  # cross diagonal
        ('A3', 'B5', 'C7'),  # cross diagonal
        ('A7', 'B5', 'C3'),  # cross diagonal
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self.first_player = self.human

    def play(self):
        self.display_welcome_message()
        self.play_match()
        self.display_goodbye_message()

    def play_match(self):
        print(f"The first player to win {TTTGame.MATCH_GOAL} "
              "games wins the match.")

        while True:
            self.play_one_game()
            self.update_match_score()
            self.display_match_score()

            if self.match_over():
                break
            if not self.play_again():
                break

            self.first_player = self.toggle_player(self.first_player)

        self.display_match_results()

    def play_one_game(self):
        current_player = self.first_player

        self.board.reset()
        self.board.display()

        while True:
            self.player_moves(current_player)
            if self.is_game_over():
                break

            self.board.display_with_clear()
            current_player = self.toggle_player(current_player)

        self.board.display_with_clear()
        self.display_results()

    def play_again(self):
        while True:
            answer = input("Play again (y/n)? ").lower()

            if answer in ["y", "n"]:
                break

            print("Sorry, that's not a valid choice.\n")

        clear_screen()
        return answer == "y"

    def player_moves(self, current_player):
        if current_player == self.human:
            self.human_moves()
        else:
            self.computer_moves()

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            printable_choices = TTTGame._join_or(valid_choices)
            prompt = f"Choose a square ({printable_choices}): "
            choice = input(prompt)
            if choice in valid_choices:
                break

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.offensive_computer_move()

        if not choice:
            choice = self.defensive_computer_move()

        if not choice:
            choice = self.pick_center_square()

        if not choice:
            choice = self.pick_random_square()

        self.board.mark_square_at(choice, self.computer.marker)

    def find_critical_square(self, player):
        for row in self.POSSIBLE_WINNING_ROWS:
            key = self.critical_square(row, player)
            if key:
                return key

        return None

    def critical_square(self, row, player):
        if self.board.count_markers_for(player, row) == 2:
            for key in row:
                if self.board.is_unused_square(key):
                    return key

        return None

    def offensive_computer_move(self):
        return self.find_critical_square(self.computer)

    def defensive_computer_move(self):
        return self.find_critical_square(self.human)

    def pick_center_square(self):
        return 'B5' if self.board.is_unused_square('B5') else None

    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def match_over(self):
        return (
            self.is_match_winner(self.human) or
            self.is_match_winner(self.computer)
        )

    def is_match_winner(self, player):
        return player.score >= TTTGame.MATCH_GOAL

    def update_match_score(self):
        if self.is_winner(self.human):
            self.human.increment_score()
        elif self.is_winner(self.computer):
            self.computer.increment_score()

    def display_match_score(self):
        human = self.human.score
        computer = self.computer.score
        print("Current match score: "
              f"[you: {human}] [computer: {computer}]")

    def display_match_results(self):
        if self.human.score > self.computer.score:
            print("You won this match! Congratulations!")
        elif self.human.score < self.computer.score:
            print("Oh, boo hoo. You lost the match!")

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def toggle_player(self, player):
        return self.computer if player == self.human else self.human

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to 3D Tic Tac Toe!")
        print("Board A is on top of Board B which is on top of Board C")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    @staticmethod
    def _join_or(choices, separator=", ", conjunction="or"):
        if len(choices) == 1:
            return str(choices[0])
        if len(choices) == 2:
            return f"{choices[0]} {conjunction} {choices[1]}"

        last = choices[-1]
        initial = choices[:-1]
        initial = [str(choice) for choice in initial]
        prompt = separator.join(initial)
        return f"{prompt}{separator}{conjunction} {last}"

game = TTTGame()
game.play()
