# Update your code from the previous question so the following code works as
# indicated:


class Game:
    count = 0

    def __init__(self, name):
        Game.count += 1
        self.name = name

    def play(self):
        return f'Start the {self.name} game!'

class Bingo(Game):
    def __init__(self, name, player):
        super().__init__(name)
        self.player_name = player

class Scrabble(Game):
    def __init__(self, name, player1, player2):
        super().__init__(name)
        self.player_name1 = player1
        self.player_name2 = player2


bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'
