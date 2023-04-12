from card_models import *
from game_models import *


class Estate(Card, Victory):
    cost = 2

    def __init__(self):
        pass


class Duchy(Card, Victory):
    cost = 5

    def __init__(self):
        pass


class Province(Card, Victory):
    cost = 8

    def __init__(self):
        pass


class Copper(Card, Treasure):
    cost = 0

    def __init__(self):
        self.cost = 0
        pass

    def on_play(self, turn):
        turn.treasure += 1


class Silver(Card, Treasure):
    cost = 3

    def __init__(self):
        self.cost = 0
        pass

    def on_play(self, player):
        player.treasure += 2


class Gold(Card, Treasure):
    cost = 6

    def __init__(self):
        self.cost = 0
        pass

    def on_play(self, player):
        player.treasure += 3


class Village(Card, Action):

    def __init__(self):
        self.cost = 3

    def on_play(self, player: Player):
        player.turn.actions += 1
        player.draw_card()


class Gardens(Card, Victory):
    def __init__(self):
        self.cost = 4


class Poacher(Card, Action):
    def __init__(self):
        self.cost = 4

    def on_play(self, player: Player):
        player.draw_card()
        player.turn.actions += 1
        player.turn.treasures += 1
        # Discard 1 for empty supply pile


class Smithy(Card, Action):
    def __init__(self):
        self.cost = 4

    def on_play(self, player: Player):
        for x in range(3):
            player.draw_card()


class ThroneRoom(Card, Action):
    def __init__(self):
        self.cost = 4

    def on_play(self, player: Player):
        # Implement Functionality
        pass


class CouncilRoom(Card, Action):
    def __init__(self):
        self.cost = 5

    def on_play(self, player: Player):
        for x in range(4):
            player.draw_card()
        player.turn.buys += 1
        # Draw other players a card


class Festival(Card, Action):
    def __init__(self):
        self.cost = 5

    def on_play(self, player: Player):
        player.turn.actions += 2
        player.turn.buys += 1
        player.turn.treasures += 2


class Laboratory(Card, Action):
    def __init__(self):
        self.cost = 5

    def on_play(self, player: Player):
        for x in range(2):
            player.draw_card()
        player.turn.actions += 1


class Market(Card, Action):
    def __init__(self):
        self.cost = 5

    def on_play(self, player: Player):
        player.draw_card()
        player.turn.actions += 1
        player.turn.buys += 1
        player.turn.treasures += 1


class Witch(Card, Action):
    def __init__(self):
        self.cost = 5

    def on_play(self, player: Player):
        for x in range(2):
            player.draw_card()
        # Give other players curses


supply = [Estate(), Duchy(), Province(), Copper(), Silver(), Gold()]

base_set = \
    [
        Village(),
        Gardens(),
        Poacher(),
        Smithy(),
        ThroneRoom(),
        CouncilRoom(),
        Festival(),
        Laboratory(),
        Market(),
        Witch(),
    ]
