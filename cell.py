class Cell:
    """Class for a square/cell on the board"""
    def __init__(self, row, col):
        self._height = None
        self._location = (row, col)
        self._worker = None

    def change_own_height(self):
        pass

    def __str__(self):
        return f"{self._height}{self._worker or ' '}" 



        # L:
        #anytime you do anything with the Worker (like move and intitalize it), you need to call something within the Board