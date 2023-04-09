from card_structures import *

basic_set = [Village]
supply = [Estate, Copper]


class Village(Card, Action):
    cost = 3

    def __init__():
        pass

    def on_play(Player):
        Player.actions += 1
        Player.drawCard()

class Estate(Card, Victory):
    cost = 2
    
    def __init__():
        pass

class Copper(Card, Treasure):
    cost = 0

    def __init__(self):
        pass

    def on_play(Player):
        Player.treasure += 1