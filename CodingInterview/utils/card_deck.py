from enum import Enum


def main():
    deck = Deck()
    print(deck)


class Rank(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __str__(self):
        return self.name.capitalize()


class Suit(Enum):
    # Bridge suit ranking
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __str__(self):
        return self.name.lower()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank.__str__() + ' of ' + self.suit.__str__()


class Deck:
    def __init__(self):
        cards = []
        for rank in Rank:
            for suit in Suit:
                cards.append(Card(rank, suit))
        self.cards = cards

    def __str__(self):
        card_list = ''
        for card in self.cards:
            card_list = card_list + card.__str__() + '\n'
        return card_list


main()


# need way to group all suited cards, all of a certain rank
# abstract properties: excluded cards, excluded suits, excluded ranks
# move Deck logic into subclass for standard deck
