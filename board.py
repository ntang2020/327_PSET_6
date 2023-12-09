from cell import Cell


class Board:
    def __init__(self):
        """Class forthe board"""
        self._matrix = [[Cell() for _ in range(5)] for _ in range(5)]

    def update_cell_height(self, row, col):
        self._matrix[row][col].update_own_height()

    def move_build(self):
        #update_workers_location() & update_workers_height() AND update_cell_height
        pass

    def board_score(self):
        pass

    def __str__(self):
        pass


    # self._workers =  self._matrix[3][2] =  Worker('A', 3, 2)
    #     Worker('B'): self._matrix[2][4], Worker('Y'): (4, 3), Worker('Z'): (4, 4)