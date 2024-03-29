from cell import Cell
from board import Board 


DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

class Worker:
    """Class for a worker piece"""
    def __init__(self, name, location,board):
        self._name = name
        self._height = 0
        self._location = location
        self._board = board
        self._my_row = self._location[0]
        self._my_col = self._location[1]
        self._previous_location = None
        self._has_moved = False

    #OR get_workers_new_location()
    def update_workers_location(self, move_direction):
        #maybe first save previous location for undo purposes
        self._previous_location = self._location

        self._location = self._location + DIRECTIONS[move_direction]

        self._has_moved = True
        

        #move_dir_row, move_dir_col = DIRECTIONS[move_direction]
        #new_row, new_col = self._my_row + move_dir_row, self._my_col + move_dir_col

        #update the worker's stored coordinates
        #self._location = (new_row, new_col)

        # return new_row, new_col

    def update_workers_height(self, new_cells_height):
        #the worker's new stored height is gonna be the height of the cell its moving to + 1
        self._height = new_cells_height + 1

    def get_build_location(self, build_direction):
        #build_dir_row, build_dir_col = DIRECTIONS[build_direction]
        #return self._my_row + build_dir_row, self._my_col + build_dir_col
        return self._location + DIRECTIONS[build_direction]
    
    #
    def undo_location_update(self):
        self._location = self._previous_location
        self._previous_location = None
        self._has_moved = False


    def enumerate_valid_moves(self):
        valid_moves = []
        for dir_coord in DIRECTIONS.values():
            if self._board.check_valid_move_dir(self._location,dir_coord):
                valid_moves.append(dir_coord)
                #or append dir
        return valid_moves
    
    



    #When you move a worker, must let the worker object know that its position has changed i.e. self.row - 1 and self.col - 1

