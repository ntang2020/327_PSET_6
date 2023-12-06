from square import Square

class Board:
    def __init__(self):
        """Class forthe board"""
        self._board = [[Square() for _ in range(5)] for _ in range(5)]

    #make this a __str__()
    def _display_board(self):
        for row in self._board:
            print(' '.join(row))
        print()

    def get_square(self, x, y):
        return self._board[x][y]





North = [-1, 0]