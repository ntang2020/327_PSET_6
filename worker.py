from cell import Square

class Worker:
    """Class for a worker piece"""
    def __init__(self, name, location):
        self._name = name
        self._height = 0
        self._location = None

        if self._name == "A":
            self._location == (3,1)


    def update_workers_location(self):
        pass

    def update_workers_height(self):
        pass

    def enumerate_valid_moves(self):
        pass

    def __str__(self):
        return self._type

    #When you move a worker, must let the worker object know that its position has changed i.e. self.row - 1 and self.col - 1


    # def move(self):
    #     pass

    # def build(self):
    #     pass