from game_models import *


class Game:

    def __init__(self) -> None:
        self.turns = 0
        self.players = []

    def setup_game(self, player_num=2):
        for x in range(player_num):
            self.players.append(Player())

        # Supply Initialization

        # Kingdom Initialization

        pass

    def is_game_over(self):
        pass

    def game_over(self):
        pass

    def game_loop(self):
        while not self.is_game_over():
            self.turns += 1
            for player in self.players:
                turn = Turn(player=player)
                player.turn = turn

                # Action Phase
                while turn.has_actions():
                    player.get_input(turn)
                    pass

                # Treasure Phase
                for card in turn.treasures:
                    card.on_play(player)

                # Buy Phase
                while turn.has_buys():
                    player.get_input(turn)
                    pass

                # Check Win Condition
                if self.is_game_over():
                    break

                # Discard & Draw
                turn.end()
        self.game_over()
