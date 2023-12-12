from worker import Worker
from board import Board
from move import Moves
from abc import ABC, abstractmethod

#Use Strategy Design Pattern where the 3 possible strategies for a Player is that they are either Human, Random, or Heuristic. Strategy is just an attribute in Player, but it’s also a class in the form of a function for Human, a function for Random, and a function for Heuristic. There are two types of Players: blue and white. And both of them could be either Human, Random, or Heuristic players. 	

class Player:
    """Class for players of the game."""
    def __init__(self, color, strategy, board):   #def __init__(self, board, strategy, workers):
        self._strategy = strategy
        self._board = board
        self._workers = self.initialize_workers(color)
    
    def initialize_workers(self, color):
        if color == 'White':
            self._color = 'White'
            self._worker_A = Worker('A', (4,2))
            self._worker_B = Worker('B', (2,4))
            self._workers = {'A': self._worker_A, 'B': self._worker_B}
        else:
            self._color = 'Blue'
            self._worker_Y = Worker('Y', (2,2))
            self._worker_Z = Worker('Z', (4,4))
            self._workers = {'Y': self._worker_Y, 'Z': self._worker_Z}
            

    #All checking the validity of moves should be done in Player’s Strategy before creating the Move object in the take_turn(). 
    def take_turn(self):  #def take_turn(self, move_direction, build_direction):
        #depens on the strategies i.e. this is different for every kind of player
        self._strategy.take_turn()

class Strategy(ABC):
    """Abstract class for all the players' strategies"""
        #get users input
        #check valid
        #do moves
    @abstractmethod
    def take_turn(self, player):   #def take_turn(self, player)
        pass

class HumanStrategy(Strategy):
    def take_turn(self, player):
        # implement human input logic: #get users input, #check valid, #do moves
        worker_choice = input("Select a worker to move")
        self._worker_choice = self._workers[worker_choice]

        move_direction_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")



        build_direction_choice = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")

        #for Human:
        #creates a Move object and (calls do_move() on it?)
        moves = Moves(self._worker_choice, self._move_direction_choice, self._build_direction_choice)
        moves.do_move()

        print(f"{self._worker_choice}, {self._move_direction_choice}, {self._build_direction_choice}")

        #return moves.do_move() ?
  

class RandomStrategy(Strategy):
    def take_turn(self, player):
        pass


class HeuristicStrategy(Strategy):
    def take_turn(self, player):
        pass

#How to use:
# player = Player(HumanStrategy(), board, 'White')
# player.take_turn()