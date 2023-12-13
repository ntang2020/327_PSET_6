from board import Board
from player import Player, Strategy, HumanStrategy, Factory


DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

#here's a game and here we are as 2 players: whose turn is it etc
class Game:
    """Manager class for the Game"""
    def __init__(self, white_player, blue_player):
        self._board = Board()
        self._white_player = white_player
        self._blue_player = blue_player
        # self._white_player = Player('White', HumanStrategy(), self._board)
        # self._blue_player = Player('Blue', HumanStrategy(), self._board)
        self._players = [self._white_player, self._blue_player]
        # self._strategy_for_players = ?? argv[1], argv[2] etc
        self._turn_number = 1
        self._curr_player = self._white_player
        self._score = None 
       

    #helpers  
    def change_player(self):
        if self._curr_player == self._white_player:
            self._curr_player = self._blue_player
        elif self._curr_player == self._blue_player:
            self._curr_player = self._white_player
        self._turn_number += 1
 
    def correct_worker(self):
        pass
    def correct_direction(self):
        pass

    def _print_board(self):
        print (self._board)

    def run(self):
        """Loop to run the game """
        self.setup()
        self._print_board()
        print(f"Turn: {self._turn_number}, Current Player: {self._curr_player._color}")

        while True:
            self._curr_player.take_turn()
            self.change_player()


            #Nicole: self._players.take_turn().do_move()

            
    #same as init?    
    def setup(self):
        # Hardcode workers on the board
        self._board._matrix[4][2]._worker = self._white_player._worker_A
        self._board._matrix[2][4]._worker = self._white_player._worker_B 
        self._board._matrix[2][2]._worker = self._blue_player._worker_Y
        self._board._matrix[4][4]._worker = self._blue_player._worker_Z

    def undo_redo(self):
        pass

    def check_win_loss(self):
        pass

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