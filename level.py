class Level:
    """Class for a level of a building"""
    def __init__(self):
        self._height = 0

    def _add_level(self):
        if self._height < 4:
            self._height = self._height + 1
        else:
            #what happens here? has the player won?
            return
    
    def __str__(self):
        return str(self._height)

