from square import Square
from worker import Worker

class Board:
    def __init__(self):
        """Class forthe board"""
        self._matrix = [[Square() for _ in range(5)] for _ in range(5)]

    #make this a __str__()
    def __str__(self):
        line = "+--+--+--+--+--+\n"
        display = line
        for row in self._matrix:
            for element in row:
                display += "|" + element.__str__()
            display += "|\n" + line 
        return display

    #def place_worker(self,row,col):


    def empty_square(self, row, col):
        if self.get_square(row,col).isEmpty():
            return True
        else: return False

        
    def get_square(self, row, col):
        return self._matrix[row][col]
    


