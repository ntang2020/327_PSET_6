from worker import Worker
from board import Board
from move import Move
from abc import ABC, abstractmethod

#Use Strategy Design Pattern where the 3 possible strategies for a Player is that they are either Human, Random, or Heuristic. Strategy is just an attribute in Player, but it’s also a class in the form of a function for Human, a function for Random, and a function for Heuristic. There are two types of Players: blue and white. And both of them could be either Human, Random, or Heuristic players. 	

class Player:
    """Class for players of the game."""
    def __init__(self, color, strategy, board):   #def __init__(self, board, strategy, workers):
        self._strategy = strategy
        self._board = board
        self._workers = self.initialize_workers(color)
    
    def initialize_workers(self, color):
        if color == 'white':
            self._color = 'white'
            self._worker_A = Worker('A', (3,1),self._board)
            self._worker_B = Worker('B', (1,3),self._board)
            self._workers = {'A': self._worker_A, 'B': self._worker_B}
        else:
            self._color = 'blue'
            self._worker_Y = Worker('Y', (1,1))
            self._worker_Z = Worker('Z', (3,3))
            self._workers = {'Y': self._worker_Y, 'Z': self._worker_Z}
    
    def get_workers(self):
        return self._workers
    
    def get_color(self):
        return self._color
    
    def get_opp_workers(self):
        '''Function to get opponent's workers'''
        if self._color == "white":
            return ["Y","Z"]
        else:
            return ["A","B"]
    
    def __str__(self):
        #ret = ''.join(self._workers.keys())
        return f"{self._color} ({''.join(self._workers.keys())})"

            
    #All checking the validity of moves should be done in Player’s Strategy before creating the Move object in the take_turn(). 
    def take_turn(self):  #def take_turn(self, move_direction, build_direction):
        #depens on the strategies i.e. this is different for every kind of player
        self._strategy.take_turn(self)

class Strategy(ABC):
    """Abstract class for all the players' strategies"""
        #get users input
        #check valid
        #do moves
    @abstractmethod
    def take_turn(self):   #def take_turn(self, player)
        pass

class HumanStrategy(Strategy):
    def take_turn(self, player):
        # implement human input logic: #get users input, #check valid, #do moves
        self._worker_choice = self._get_worker_choice(player)

        self._move_direction_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)")

        self._build_direction_choice = input("Select a direction to build (n, ne, e, se, s, sw, w, nw)")

        #for Human:
        #creates a Move object and (calls do_move() on it?)
        move = Move(self._worker_choice, self._move_direction_choice, self._build_direction_choice)
        move.do_move()


        print(f"{self._worker_choice}, {self._move_direction_choice}, {self._build_direction_choice}")

        return move
    
    def _get_worker_choice(self, player):
        worker_choice = input("Select a worker to move\n")
        if worker_choice in player.get_workers():
            return worker_choice
        else:
            if worker_choice in player.get_opp_workers():
                print("That is not your worker")
            else: 
                print("Not a valid worker")
            self._get_worker_choice()
    
    def _get_move_choice(self,player):
        move_choice = input("Select a direction to move (n, ne, e, se, s, sw, w, nw)\n")
        if move_choice not in ['n','ne','e','se','s','sw','w','nw']:
            print("Not a valid direction")
        else: 
            return


  

class RandomStrategy(Strategy):
    def take_turn(self):
        pass


class HeuristicStrategy(Strategy):
    def take_turn(self):
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