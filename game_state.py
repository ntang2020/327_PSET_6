from board import Board

DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}


class Game_State:
    """Manager class for the game"""
    def __init__(self, board, workers):
        self._board = Board()
        self._turn_number = 1
        self._curr_player = None    #OR curr_player = 'White' ?
        self._score = None   

    def change_player(self):
        pass
    def correct_worker(self):
        pass
    def correct_direction(self):
        pass

    


    # #to be displayed at the start of each turn
    # def _display(self):
    #     self._board._display_board()
    #     print(f"{self._turn_number}, {self._curr_player}, {self._score}")

    