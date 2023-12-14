from board import Board

class Moves:
    """Class for a worker's moves.  class for this Command Design Pattern"""
    def __init__(self, worker, move_direction, build_direction, board):
        #Maybe here set = to actual objects
        self._worker = worker
        self._move_direction = move_direction
        self._build_direction = build_direction
        self._board = board



    def do_move(self):
        #calls move_build on the board
    
        self._board.move_build(self._worker, self._move_direction, self._build_direction)
        

    def undo_move(self):
        pass


