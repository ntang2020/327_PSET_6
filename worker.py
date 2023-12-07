from square import Square
from exceptions import *
from board import Board


class Worker:
    """Class for a worker piece"""
    def __init__(self, letter):
        self._letter = letter #ABZY
        self._curr_square = None
        #self._coord = None
        self.COORD_LIMIT = 4

        if letter == "A":
            self._coord = (3,1)
        elif letter == "B":
            self._coord = (1,3)
        elif letter == "Y":
            self._coord = (1,1)
        elif letter == "Z": #else:
            self._coord = (3,3)
    
    def move(self, direction):
        
        return 

    def _check_valid_move(self,direction):
        new_coord = self._coord + direction
        if new_coord[0] > self.COORD_LIMIT or new_coord[1] > self.COORD_LIMIT:
            raise InvalidMove()
        
        



        



    

    def get_letter(self): #alt could make into a string method
        return self._letter
    
    

