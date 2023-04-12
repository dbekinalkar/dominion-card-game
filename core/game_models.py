from random import shuffle


class Player:
    def __init__(self) -> None:
        self.deck = Deck()
        self.hand = Hand()
        self.discard = Deck()

        self.turn = None

    def draw_card(self):
        pass


class Turn:
    def __init__(self, player=None):
        self.treasures = 0
        self.player = None

    def has_actions(self):
        pass

    def has_buys(self):
        pass

    def end(self):
        pass


class Pile:
    pass


class Deck(list):

    def shuffle(self):
        self.cards = shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

    def topdeck(self, card):
        self.cards.append(card)

    def draw(self, player, num):
        pass

    pass


class Battlefield:
    def __init__(self):
        self.actions = []
        self.treasures = []

    pass


class Hand:
    pass


class Supply:
    pass


class Kingdom:
    pass
