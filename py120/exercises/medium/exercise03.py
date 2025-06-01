from math import log2
from random import randint


class GuessingGame:
    def __init__(self, low=1, high=100):
        self._low = low
        self._high = high
        self._number_of_guesses = int(log2(high - low + 1)) + 1
        self._winning_number = None
        self._player_guess = None

    def play(self):
        self._run_game()
        if self._player_guess == self._winning_number:
            self._display_win()
        else:
            self._display_loss()

    def _run_game(self):
        self._winning_number = randint(self._low, self._high)
        for guess in range(self._number_of_guesses, 0, -1):
            self._display_remaining_guesses(guess)
            self._player_guess = self._ask_for_number()
            if self._player_guess == self._winning_number:
                break
            self._give_hint()

    def _display_remaining_guesses(self, guess):
        if guess == 1:
            print(f'You have {guess} guess remaining.')
        else:
            print(f'You have {guess} guesses remaining.')

    def _display_enter_number(self):
        return f'Enter a number between {self._low} and {self._high}. '

    def _ask_for_number(self):
        guess = input(self._display_enter_number())
        while not self._is_valid_guess(guess):
            guess = input(f'Invalid guess. '
                          f'{self._display_enter_number()}')
        return int(guess)

    def _is_valid_guess(self, guess):
        return guess.isnumeric() and \
               self._low <= int(guess) <= self._high

    def _give_hint(self):
        if self._player_guess > self._winning_number:
            print('Your guess is too high.\n')
        else:
            print('Your guess is too low.\n')

    def _display_win(self):
        print('That\'s the number!\n\nYou won!\n')

    def _display_loss(self):
        print('You have no more guesses. You lost!')
        print(f'The mystery number was: {self._winning_number}\n')


game = GuessingGame(501, 1500)
game.play()

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 104
# Invalid guess. Enter a number between 501 and 1500: 1000
# Your guess is too low.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 1250
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 1375
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 80
# Invalid guess. Enter a number between 501 and 1500: 1312
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 1343
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 1359
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 1351
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 1355
# That's the number!

# You won!

game.play()

# You have 10 guesses remaining.
# Enter a number between 501 and 1500: 1000
# Your guess is too high.

# You have 9 guesses remaining.
# Enter a number between 501 and 1500: 750
# Your guess is too low.

# You have 8 guesses remaining.
# Enter a number between 501 and 1500: 875
# Your guess is too high.

# You have 7 guesses remaining.
# Enter a number between 501 and 1500: 812
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 501 and 1500: 843
# Your guess is too high.

# You have 5 guesses remaining.
# Enter a number between 501 and 1500: 820
# Your guess is too low.

# You have 4 guesses remaining.
# Enter a number between 501 and 1500: 830
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 501 and 1500: 835
# Your guess is too low.

# You have 2 guesses remaining.
# Enter a number between 501 and 1500: 836
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 501 and 1500: 837
# Your guess is too low.

# You have no more guesses. You lost!
