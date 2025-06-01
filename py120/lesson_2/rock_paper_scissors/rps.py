import random


class Player:
    CHOICES = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }

    def __init__(self):
        self.move = None
        self.score = 0

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

class Human(Player):
    def choose(self):
        prompt = 'Please choose rock, paper, or scissors (r/p/s): '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = Player.CHOICES[choice]

class Computer(Player):
    def choose(self):
        self.move = random.choice(list(Player.CHOICES.values()))

class RPSGame:
    MAX_SCORE = 3

    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _compute_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            self._human.add_score()
            print('You win!')
        elif self._computer_wins():
            self._computer.add_score()
            print('Computer wins!')
        else:
            print("It's a tie")

        print(f'SCORE you: {self._human.score} computer: {self._computer.score}')

    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()
        while True:
            self._play_match()
            if not self._play_again():
                break
        self._display_goodbye_message()

    def _play_match(self):
        self._reset_scores()
        while not self._match_over():
            self._human.choose()
            self._computer.choose()
            self._compute_winner()

    def _reset_scores(self):
        self._human.reset_score()
        self._computer.reset_score()

    def _match_over(self):
        return (self._human.score == RPSGame.MAX_SCORE or
                self._computer.score == RPSGame.MAX_SCORE)


RPSGame().play()
