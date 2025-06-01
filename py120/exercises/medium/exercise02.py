from random import randint


class GuessingGame:
    NUMBER_OF_GUESSES = 7
    MIN = 1
    MAX = 100

    def play(self):
        self.winning_numer = randint(GuessingGame.MIN,
                                     GuessingGame.MAX)
        for guess in range(GuessingGame.NUMBER_OF_GUESSES, 0, -1):
            self._display_remaining_guesses(guess)
            self.player_guess = self._ask_for_number()
            if self.player_guess == self.winning_numer:
                break
            self._give_hint()

        if self.player_guess == self.winning_numer:
            self._display_win()
        else:
            self._display_loss()

    def _display_remaining_guesses(self, guess):
        if guess == 1:
            print(f'You have {guess} guess remaining.')
        else:
            print(f'You have {guess} guesses remaining.')

    @classmethod
    def _display_enter_number(cls):
        return f'Enter a number between {cls.MIN} and {cls.MAX}. '

    def _ask_for_number(self):
        guess = input(GuessingGame._display_enter_number())
        while not self._is_valid_guess(guess):
            guess = input(f'Invalid guess. '
                          f'{GuessingGame._display_enter_number()}')
        return int(guess)

    def _is_valid_guess(self, guess):
        return guess.isnumeric() and \
               GuessingGame.MIN <= int(guess) <= GuessingGame.MAX

    def _give_hint(self):
        if self.player_guess > self.winning_numer:
            print('Your guess is too high.\n')
        else:
            print('Your guess is too low.\n')

    def _display_win(self):
        print('That\'s the number!\nYou won!\n')

    def _display_loss(self):
        print('You have no more guesses. You lost!\n')


game = GuessingGame()
game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 104
# Invalid guess. Enter a number between 1 and 100: 50
# Your guess is too low.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 75
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 85
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 0
# Invalid guess. Enter a number between 1 and 100: 80
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 81
# That's the number!

# You won!

game.play()

# You have 7 guesses remaining.
# Enter a number between 1 and 100: 50
# Your guess is too high.

# You have 6 guesses remaining.
# Enter a number between 1 and 100: 25
# Your guess is too low.

# You have 5 guesses remaining.
# Enter a number between 1 and 100: 37
# Your guess is too high.

# You have 4 guesses remaining.
# Enter a number between 1 and 100: 31
# Your guess is too low.

# You have 3 guesses remaining.
# Enter a number between 1 and 100: 34
# Your guess is too high.

# You have 2 guesses remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have 1 guess remaining.
# Enter a number between 1 and 100: 32
# Your guess is too low.

# You have no more guesses. You lost!
