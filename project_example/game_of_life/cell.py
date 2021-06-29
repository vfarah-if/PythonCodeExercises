class Cell:
    """
    Represent single unit of life
    """

    def __init__(self, is_alive=False):
        self.is_alive = is_alive
        self.neighbours = list()

    def re_generate(self):
        def is_overpopulated():
            return len(alive_neighbours) > 3

        def is_underpopulated():
            return len(alive_neighbours) < 2

        def is_thriving():
            return self.is_alive and len(alive_neighbours) >= 2

        def is_fertile():
            return not self.is_alive and len(alive_neighbours) == 3

        alive_neighbours = [neighbour for neighbour in self.neighbours if neighbour.is_alive]
        if is_thriving() or is_fertile():
            self.is_alive = True
        if is_underpopulated() or is_overpopulated():
            self.is_alive = False

    def add_neighbour(self, neighbour):
        """Append neighbour"""
        self.neighbours.append(neighbour)

    def __str__(self):
        return 'X' if self.is_alive else ' '
