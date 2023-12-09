from board import Board

class Moves:
    """Class for a worker's moves. Invoker class for this Command Design Pattern"""
    def __init__(self, worker, move_direction, build_direction):
        # self._board = Board()
        self._worker = worker
        self._move_direction = move_direction
        self._build_direction = build_direction


    def do_move(self, board):
        #calls move_build on the board
        board.move_build()
        pass

    def undo_move(self):
        pass


