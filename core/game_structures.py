from random import shuffle

class Player:
    def __init__(self) -> None:
        self.deck = Deck()
        self.hand = Hand()
        self.discard = Deck()
        pass
    pass


class Turn:
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
    pass


class Hand:
    pass

class Supply:
    pass


class Kingdom:
    pass
