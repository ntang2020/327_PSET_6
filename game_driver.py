from game_state import Game_State
from board import Board

class Game_Driver():
    
    def __init__(self):
        #self.board = Board()
        self.game_state = Game_State()
        

    def run(self):
        # game_state.start_game()
        self.game_state.display()
    
    def select_worker(self):
        worker = input("Select a worker to move\n")
        # game_state check_valid_worker 


