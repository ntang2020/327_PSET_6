from cell import Cell
from exceptions import *



class Board:
    def __init__(self):
        """Class for the board"""
        self._matrix = [[Cell(row, col) for col in range(5)] for row in range(5)]
        self._BOARD_LIMIT = 4

    def update_cell_height(self, row, col):
        self._matrix[row][col].update_own_height()

    def move_build(self, worker, move_direction, build_direction):
        #call update_workers_location() & update_workers_height() AND update_cell_height

        #first change the worker's location i.e. update its stored coordinates
        changed_worker = worker.update_workers_location(move_direction)
        #get the coordinates of the worker's new cell
        new_row = changed_worker._my_row
        new_col = changed_worker._my_col
        new_cell = self._matrix[new_row][new_col]

        changed_worker.update_workers_height(new_cell._height) #update the worker's stored height

        #Reflect changes on the board:
        #update the current cell to None
        previous_cell = self._matrix[worker._previous_location[0]][worker._previous_location[1]]
        previous_cell._worker = None

        # Finish moving worker to the new cell
        new_cell._worker = changed_worker          #If I used a set_worker_on_cell(), it would be new_cell.set_worker_on_cell(changed_worker)
       
        #THEN EXECTUTE BUILD
        build_row, build_col = new_cell._worker.get_build_location(build_direction)
        self.update_cell_height(build_row, build_col)

    def check_valid_move_dir(self,location,move_dir):
        new_location = location + move_dir
        '''Check new location is on the board'''
        if 0 <= new_location[0] <= self._BOARD_LIMIT and 0 <= new_location[1] <= self._BOARD_LIMIT:
            new_cell = self._get_cell_on_board(new_location)
            '''Check if new location has worker on it'''
            if not new_cell.check_worker_on_cell():
                height_diff = new_cell.get_cell_height() - self._get_cell_on_board(location).get_cell_height()
                '''Check proper height difference (can only move up 1, can move down any distance)'''
                if height_diff <= 1: 
                    return True
        return False 
    
    def check_win(self):
        for row in self._matrix:
            for col in row:
                if self._get_cell_on_board((row,col)).get_cell_height() == 3: #>2
                    return True
        return False




    
    def _get_cell_on_board(self,location):
        return self._matrix[location[0]][location[1]]



    def __str__(self):
        board_output = []
        for row in self._matrix:
            row_s = '|'.join(str(cell) for cell in row)
            board_output.append("+---+---+---+---+---+")
            board_output.append(f"|{row_s}|")
        board_output.append("+---+---+---+---+---+")
        return '\n'.join(board_output)

    

    def board_score(self):
        pass

    