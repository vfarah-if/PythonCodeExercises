from game_of_life.cell_state import CellState


class Cell:

    def __init__(self, current_state=CellState.Dead):
        self.current_state = current_state
        self.neighbours = list()

    def next_state(self) -> CellState:
        def is_overpopulated():
            return alive_cell_count > 3

        def is_underpopulated():
            return alive_cell_count < 2

        def is_thriving():
            return self.current_state is CellState.Alive and alive_cell_count == 2

        def is_fertile():
            return self.current_state is CellState.Dead and alive_cell_count == 3

        next_state = self.current_state
        alive_cell_count = len([neighbour for neighbour in self.neighbours if neighbour.current_state is CellState.Alive])
        if is_thriving() or is_fertile():
            next_state = CellState.Alive
        if is_underpopulated() or is_overpopulated():
            next_state = CellState.Dead
        return next_state

    def add_neighbours(self, neighbours: list):
        for neighbour in neighbours:
            self.neighbours.append(neighbour)

    def __str__(self):
        return 'X' if self.current_state is CellState.Alive else ' '
