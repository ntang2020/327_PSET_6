
DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

class Cell:
    """Class for a square/cell on the board"""
    def __init__(self, row, col, worker=None):
        self._height = 0
        self._location = (row, col)
        self._worker = worker

    def check_worker_on_cell(self):
        #return self._worker
        if self._worker: 
            return True
        else:
            return False
    
    def get_cell_height(self):
        return self._height

    #build a level
    def update_own_height(self):  #def update_own_height(self, build_direction)
        if self._height < 4:
            self._height = self._height + 1

    def set_worker_on_cell(self, worker):
        self._worker = worker
    
    def remove_worker_on_cell(self):
        #return self._worker
        self._worker = None

    def __str__(self):
        if self._worker:
            workers_name = self._worker._name
        else:
            workers_name = ' '
        return f"{self._height}{workers_name}"



        # L:
        #anytime you do anything with the Worker (like move and intitalize it), you need to call something within the Board