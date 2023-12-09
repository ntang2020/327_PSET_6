from worker import Worker
from board import Board

#Use Strategy Design Pattern where the 3 possible strategies for a Player is that they are either Human, Random, or Heuristic. Strategy is just an attribute in Player, but it’s also a class in the form of a function for Human, a function for Random, and a function for Heuristic	

class Player:
    """Class for players of the game."""
    def __init__(self):
        self._color = color
        self._worker = Worker(name)
        self._board = Board()
        self._strategy = strategy


    #All checking the validity of moves should be done in Player’s Strategy before creating the Move object in the take_turn(). 
    def take_turn(self, move_direction, build_direction):
        #depens on the strategies i.e. this is different for every kind of player
        #for Human:
        #creates a Move object and calls do_move() on it
        pass


class Strategy:

    def __call__():
        #get users input
        #check valid
        #do moves



class White_Player(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._color = "White"
        self._worker_A = Worker("A")
        self._worker_B = Worker("B")


class Blue_Player(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._color = "Blue"
        self._worker_Y = Worker("Y")
        self._worker_Z = Worker("Z")
