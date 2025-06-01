from random import shuffle


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.shuffle_deck()

    def shuffle_deck(self):
        self._cards = [Card(rank, suit) for rank in Deck.RANKS
                                        for suit in Deck.SUITS]
        shuffle(self._cards)

    def draw(self):
        if not self._cards:
            self.shuffle_deck()

        return self._cards.pop()


class Card:
    COURT = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def _get_rank(self):
        return self.__class__.COURT.get(self.rank, self.rank)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self.rank == other.rank

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        return self._get_rank() < other._get_rank()

    def __str__(self):
        return f'{self.rank} of {self.suit}'


deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).
