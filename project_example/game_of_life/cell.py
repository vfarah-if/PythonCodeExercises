class Cell:
    """
    Represent single unit of life
    """

    neighbours = list()

    def __init__(self, x: int, y: int, is_alive=False):
        self.x = x
        self.y = y
        self.is_alive = is_alive

    def re_generate(self):
        alive_neighbours = [neighbour for neighbour in self.neighbours if neighbour.is_alive]
        if len(alive_neighbours) == 3:
            self.is_alive = True
        if len(alive_neighbours) < 2:
            self.is_alive = False
