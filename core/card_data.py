from card_structures import * 


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

    def on_play(Turn):
        Turn.treasure += 1

class Silver(Card, Treasure):
    cost = 3

    def __init__(self):
        self.cost = 0
        pass

    def on_play(Player):
        Player.treasure += 2

class Gold(Card, Treasure):
    cost = 6

    def __init__(self):
        self.cost = 0
        pass

    def on_play(Player):
        Player.treasure += 3

class Village(Card, Action):
    
    def __init__(self):
        self.cost = 3

    def on_play(Player):
        Player.actions += 1
        Player.drawCard()


supply = [Estate(), Duchy(), Province(), Copper(), Silver(), Gold()]

basic_set = [Village()]
