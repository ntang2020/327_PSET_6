from cell import Cell


class Board:
    def __init__(self):
        """Class for the board"""
        self._matrix = [[Cell(row, col) for col in range(5)] for row in range(5)]

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


    def __str__(self):
        board_output = []
        for row in self._matrix:
            row_s = '|'.join(str(cell) for cell in row)
            board_output.append("+---+---+---+---+---+")
            board_output.append(f"| {row_s} |")
        board_output.append("+---+---+---+---+---+")
        return '\n'.join(board_output)

    def board_score(self):
        pass

    