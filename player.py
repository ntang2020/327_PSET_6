from worker import Worker

class Player:
    
    def __init__(self,color):
        self.color = color
        self.workers = [] 
        if color == "white":
            self.workers = {"A": Worker("A"), "B":Worker("B")}
        elif color == "blue": #or just else:
            self.workers = {"Y": Worker("Y"), "Z": Worker("Z")}
    
    def __str__(self):
        if self.color == "white":
            return self.color + " (AB)"
        else:
            return self.color + " YZ"
    
    def check_worker(self,letter):
        if self.workers.get(letter):
            return True
        else: return False
    
   #def move_worker(self, letter):




        
    
