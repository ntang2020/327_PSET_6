from board import Board
from player import Player


DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

#here's a game and here we are as 2 players: whose turn is it etc
class Game:
    """Manager class for the Game"""
    def __init__(self):
        self._board = Board()
        self._players = Player()
        self._strategy_for_players = ??
        self._turn_number = 1
        self._curr_player = None    #OR curr_player = 'White' ?
        self._score = None 

        self._white_player = White_Player()
        self._blue_player = Blue_Player()

    #helpers  
    def change_player(self):
        pass
    def correct_worker(self):
        pass
    def correct_direction(self):
        pass

    def _print_board(self):
        print (self._board)

    def run(self):
        """Loop to run the game """
        while True:
            self._print_board()
            worker_choice = input("Select a worker to move")
            move_direction_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")
            build_direction_choice = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")

            self._players.take_turn(move_direction_choice, build_direction_choice)


            print(f"{worker_choice}, {move_direction_choice}, {build_direction_choice}")
            worker_choice.move(move_direction_choice, build_direction_choice)
            
    #same as init?    
    def setup(self):
        pass

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
        self._deep_copy = deep_copy

    


    #The state machine from Perry: So the Move class in the CLI will take user input THEN CALL the move method in the Game file