from game_structures import *

class Game:
    
    def __init__(self) -> None:
        self.players = []
    
    def setup_game(self, playerNum = 2):
        for x in playerNum:
            self.players.append(Player())
            
        # Supply Initialization
        
        # Kingdom Initialization

        
        pass


    def is_game_over(self):
        return False

    def game_over(self):
        pass


    def game_loop(self):
        while not self.is_game_over():
            self.turns += 1
            for player in self.players:
                turn = Turn(player)
                player.turn = turn
                
                # Action Phase
                while(turn.has_actions()):
                    bot.get_input(turn)
                    pass


                # Tresure Phase
                for card in turn.treasures:
                    card.on_play(player)
                
                # Buy Phase
                while(turn.has_buys()):
                    bot.get_input(turn)
                    pass

                # Check Win Condition
                if(self.is_game_over()):
                    break

                # Discard & Draw
                turn.end()
        self.game_over()