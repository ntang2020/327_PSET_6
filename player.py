from worker import Worker
from board import Board
from move import Moves

#Use Strategy Design Pattern where the 3 possible strategies for a Player is that they are either Human, Random, or Heuristic. Strategy is just an attribute in Player, but it’s also a class in the form of a function for Human, a function for Random, and a function for Heuristic	

class Player:
    """Class for players of the game."""
    def __init__(self, board, strategy):
        self._strategy = strategy


    #All checking the validity of moves should be done in Player’s Strategy before creating the Move object in the take_turn(). 
    def take_turn(self, move_direction, build_direction):
        #depens on the strategies i.e. this is different for every kind of player
        #for Human:
        #creates a Move object and calls do_move() on it
        moves = Moves(self._worker, move_direction, build_direction)
        moves.do_move()
        pass




class WhitePlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._color = "White"
        self._workers = [Worker('A', (3,1)), Worker('B')]


class BluePlayer(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._color = "Blue"
        self._workers = [Worker('Y'), Worker('Z')]


class Strategy:

   
        #get users input
        #check valid
        #do moves
    def take_turn(self, player):
        pass

class HumanStrategy(Strategy):
    def take_turn(self, player):
        # implement human input logic
        worker_choice = input("Select a worker to move")
        move_direction_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")
        build_direction_choice = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")

        moves = Moves(self._worker, move_direction_choice, build_direction_choice)
        moves.do_move()

        pass