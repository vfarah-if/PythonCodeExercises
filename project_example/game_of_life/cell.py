from game_of_life.cell_state import CellState


class Cell:
    """
    Represent single unit of life
    """

    def __init__(self, current_state=CellState.Dead):
        self.current_state = current_state
        self.next_state = current_state
        self.neighbours = list()

    def get_next_state(self) -> CellState:
        def is_overpopulated():
            return len(alive_neighbours) > 3

        def is_underpopulated():
            return len(alive_neighbours) < 2

        def is_thriving():
            return self.current_state is CellState.Alive and len(alive_neighbours) == 2

        def is_fertile():
            return self.current_state is CellState.Dead and len(alive_neighbours) == 3

        self.next_state = self.current_state
        alive_neighbours = [neighbour for neighbour in self.neighbours if neighbour.current_state is CellState.Alive]
        if is_thriving() or is_fertile():
            self.next_state = CellState.Alive
        if is_underpopulated() or is_overpopulated():
            self.next_state = CellState.Dead
        return self.next_state

    def transfer_state(self):
        self.current_state = self.next_state

    def add_neighbour(self, neighbour):
        """Append neighbour"""
        self.neighbours.append(neighbour)

    def __str__(self):
        return 'X' if self.current_state is CellState.Alive else ' '
