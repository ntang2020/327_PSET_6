from board import Board
from player import Player, Strategy, HumanStrategy, Factory
from move import Move, MoveStack


DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

#here's a game and here we are as 2 players: whose turn is it etc
class Game:
    """Manager class for the Game"""
    def __init__(self, white_player, blue_player, undo_redo = "off", score_display = "off"):
        self._board = Board()
        self._white_player = white_player
        self._blue_player = blue_player
        
        if undo_redo == "on":
            self._undo_redo = True
        else: 
            self._undo_redo = False
        
        if score_display == "on":
            self._score_display = True
        else: 
            self._score_display = False
        

        # self._white_player = Player('White', HumanStrategy(), self._board)
        # self._blue_player = Player('Blue', HumanStrategy(), self._board)
        self._players = [self._white_player, self._blue_player]
        # self._strategy_for_players = ?? argv[1], argv[2] etc
        self._turn_number = 1
        self._curr_player = None
        self._score = None 
        self._moves = MoveStack()
       
    def _change_player(self):
        if self._curr_player == self._white_player:
            self._curr_player = self._blue_player
        else:
            self._curr_player = self._white_player
        self._turn_number += 1
 
    def _print_board(self):
        print (self._board)

    def run(self):
        """Loop to run the game """
        self.setup()

        while True:
            self._print_board()
            print(f"Turn: {self._turn_number}, {self._curr_player.__str__()}")
            '''Check if player has won (height of 3)'''
            if self.check_win_loss():
                #if True, previous player has won 
                self._change_player()
                print(f"{self._curr_player.get_color()} has won")
                play_again = input("Play again?\n")
                if play_again == "yes":
                    self.run()
                else: 
                    break
            self._moves.push(self._curr_player.take_turn())
            self._change_player()

            
    #same as init?    
    def setup(self):
        # Hardcode workers on the board
        self._curr_player = self._white_player
        self._board._matrix[3][1]._worker = self._white_player._worker_A
        self._board._matrix[1][3]._worker = self._white_player._worker_B 
        self._board._matrix[1][1]._worker = self._blue_player._worker_Y
        self._board._matrix[3][3]._worker = self._blue_player._worker_Z

    def undo_redo(self):
        pass

    def check_win_loss(self):
        return self._board.check_win()

    def save_game(self):
        #called every turn
        #stack of Moves
        pass

    def load_game(self, deep_copy):
        #set all attributes to attributes of the deep copy
        # self._deep_copy = deep_copy the
        pass

    # def main():
    #     factory = Factory()
    #     white_player = factory.create_players('White', 'human')
    #     blue_player = factory.create_players('Blue', 'human')
    #     Game(white_player, blue_player).run()


    # if __name__ == "__main__":
    #     main()



    #The state machine from Perry: So the Move class in the CLI will take user input THEN CALL the move method in the Game file