from cell import Square

class Worker:
    """Class for a worker piece"""
    def __init__(self, name):
        self._name = name
        self._height = None
        self._location =

    def update_workers_location(self):
        pass

    def update_workers_height(self):
        pass

    def get_valid_moves(self):
        pass

    def __str__(self):
        return self._type

    #When you move a worker, must let the worker object know that its position has changed i.e. self.row - 1 and self.col - 1

    
    # def move(self):
    #     pass

    # def build(self):
    #     pass