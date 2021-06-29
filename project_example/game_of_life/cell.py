class Cell:
    """
    Represent single unit of life
    """

    def __init__(self, x: int, y: int, is_alive=False):
        self.x = x
        self.y = y
        self.is_alive = is_alive
