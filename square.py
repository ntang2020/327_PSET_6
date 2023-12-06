from level import Level


class Square:
    """Class for a square on the board"""
    def __init__(self):
        self._level = Level()
        self._worker = None