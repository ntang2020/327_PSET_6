from board import Board
from player import Player

DIRECTIONS = {
    'n': (-1, 0), 'ne': (-1, 1), 'e': (0, 1), 'se': (1, 1),
    's': (1, 0), 'sw': (1, -1), 'w': (0, -1), 'nw': (-1, -1)}


class Game_State:
    """Manager class for the game"""
    def __init__(self):
        self._board = Board()
        self._turn_number = 1
        
        self._curr_worker = None
        self._score = None   
        self._players = {"white": Player("white"), "blue": Player("blue")}
        self._curr_player = self._players["white"]    #OR curr_player = 'White' ?

    def start_game(self):
        #instantiate workers & players
        pass
    
    def display(self):
        ret = f"Turn: {str(self._turn_number)}, {self._curr_player.__str__()})"
        return self._board.__str__() + ret

    def select_worker(self,letter):
        if self._curr_player.check_worker(letter):
            return 


    def change_player(self):
        if self._curr_player == self._players["white"]:
            self._curr_player = self._players["blue"]
            #self._curr_workers = "YZ"
        else: 
            self._curr_player = self._players["white"]
            #self._curr_workers = "AB"
    
    def correct_worker(self):
        pass
    
    def correct_direction(self):
        pass

    


    # #to be displayed at the start of each turn
    # def _display(self):
    #     self._board._display_board()
    #     print(f"{self._turn_number}, {self._curr_player}, {self._score}")

    