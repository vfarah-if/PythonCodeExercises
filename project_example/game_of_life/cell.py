class Cell:
    """
    Represent single unit of life
    """

    def __init__(self, x: int, y: int, is_alive=False):
        self.x = x
        self.y = y
        self.is_alive = is_alive
        self.neighbours = list()

    def re_generate(self):
        alive_neighbours = [neighbour for neighbour in self.neighbours if neighbour.is_alive]
        if (self.is_alive and len(alive_neighbours) >= 2) or (len(alive_neighbours) == 3):
            self.is_alive = True
        if len(alive_neighbours) < 2:
            self.is_alive = False
