DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}

from worker import Worker
from board import Board
from move import Moves
from abc import ABC, abstractmethod

#Use Strategy Design Pattern where the 3 possible strategies for a Player is that they are either Human, Random, or Heuristic. Strategy is just an attribute in Player, but it’s also a class in the form of a function for Human, a function for Random, and a function for Heuristic. There are two types of Players: blue and white. And both of them could be either Human, Random, or Heuristic players. 	

class Player:
    """Class for players of the game."""
    def __init__(self, color, strategy):   #def __init__(self, board, strategy, workers):
        self._strategy = strategy
        # self._board = Board()
        self.initialize_workers(color)
    
    def initialize_workers(self, color):
        if color == 'White':
            self._color = 'White'
            self._worker_A = Worker('A', (3,1))
            self._worker_B = Worker('B', (1,3))
            self.workers = {'A': self._worker_A, 'B': self._worker_B}
        else:
            self._color = 'Blue'
            self._worker_Y = Worker('Y', (1,1))
            self._worker_Z = Worker('Z', (3,3))
            self.workers = {'Y': self._worker_Y, 'Z': self._worker_Z}
            
    #All checking the validity of moves should be done in Player’s Strategy before creating the Move object in the take_turn(). 
    def take_turn(self, board):  #def take_turn(self, move_direction, build_direction):
        #depens on the strategies i.e. this is different for every kind of player
        self._strategy.take_turn(board, self)

class Strategy(ABC):
    """Abstract class for all the players' strategies"""
        #get users input
        #check valid
        #do moves
    @abstractmethod
    def take_turn(self, board, player):   #def take_turn(self, player)
        pass

class HumanStrategy(Strategy):
    def take_turn(self, board, player):
        # implement human input logic: #get users input, #check valid, #do moves
        worker_choice = input("Select a worker to move")
        self._worker_choice = player.workers[worker_choice]

        move_direction_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")
        self._move_direction_choice = DIRECTIONS[move_direction_choice]


        build_direction_choice = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")
        self._build_direction_choice = DIRECTIONS[build_direction_choice]

        #for Human:
        #creates a Move object and (calls do_move() on it?)
        moves = Moves(self._worker_choice, self._move_direction_choice, self._build_direction_choice, board)
        moves.do_move()

        print(f"{worker_choice},{move_direction_choice},{build_direction_choice}")

        #return moves.do_move() ?
  

class RandomStrategy(Strategy):
    def take_turn(self, board, player):
        pass


class HeuristicStrategy(Strategy):
    def take_turn(self, board, player):
        pass

#How to use:
# player = Player(HumanStrategy(), board, 'White')
# player.take_turn()

class Factory:
    def create_players(self, color, strategy):
        if strategy == 'human':
            return Player(color, HumanStrategy())
        elif strategy == 'random':
            return Player(color, RandomStrategy())
        elif strategy == 'heuristic':
            return Player(color, HeuristicStrategy())