from level import Level


class Square:
    """Class for a square on the board"""
    def __init__(self):
        self._level = Level()
        self._worker = None
    
    def isEmpty(self):
        if self._worker:
            return False
        else:
            return True


    def __str__(self):
        ret = self._level.__str__()
        if self._worker:
            ret += str(self._worker.get_letter())
        else: 
            ret += " "
        return ret


