from os import linesep

from game_of_life.cell import Cell
from game_of_life.cell_state import CellState
from game_of_life.position import Position


class Generator:
    """
    Game of life generator
    """

    def __init__(self, size: int, seed_data: list = list()):
        """
        Constructor

        @param size: Board Size or matrix setting for x and y and must be minimum 2
        @param seed_data: List of tuples denoting x, y positions
        """
        if size < 2:
            raise ValueError('"size" must must be no less than 2 for life to exist', size)
        self.size = size
        self.board = [[Cell() for _ in range(self.size)] for _ in range(self.size)]
        self.next_states = [[CellState.Dead] * self.size for _ in range(self.size)]
        self._setup_neighbours()
        self._seed(seed_data)

    def tick(self):
        """Regenerates all data in the cells generating the patterns from the seeded data"""
        self._calculate_life_expectancy()
        self._regenerate()

    def cell(self, x: int, y: int) -> Cell:
        """Get cell on board by position"""
        return self.board[y][x]

    def is_on_board(self, x, y) -> bool:
        """
        Checks position is valid

        @return: True if in range, false if not
        """
        return 0 <= x < self.size and 0 <= y < self.size

    def board_positions(self) -> list[Position]:
        """
        Gets all board positions grid positions one rwo at a time

        @return: list of Position
        """
        positions = list()
        for y in range(self.size):
            for x in range(self.size):
                positions.append(Position(x, y))
        return positions

    def __str__(self) -> str:
        """
        Overrides default string output to represent a simplified visual of what is generated

        @return: Visual string showing a grid of cells showing the state making this easier to test
        """
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += f'{linesep} | '
            for x in range(self.size):
                item = str(self.cell(x, y))
                result += f'{item} | '
        return result

    def _regenerate(self):
        for pos in self.board_positions():
            self.cell(pos.x, pos.y).current_state = self.next_states[pos.y][pos.x]

    def _calculate_life_expectancy(selrefactoref):
        for pos in self.board_positions():
            self.next_states[pos.y][pos.x] = self.cell(pos.x, pos.y).next_state()

    def _setup_neighbours(self):
        for pos in self.board_positions():
            for neighbour in self._neighbours_by_position(pos.x, pos.y):
                self.cell(pos.x, pos.y).add_neighbour(neighbour)

    def _seed(self, positions: list):
        for item in positions:
            x = item[0]
            y = item[1]
            if not self.is_on_board(x, y):
                message = f"[{x}, {y}] should have values in the range of 0 - {self.size - 1}"
                raise ValueError(message, x, y)
            self.cell(x, y).current_state = CellState.Alive

    def _neighbours_by_position(self, x, y) -> list[Cell]:
        y_range = [y - 1, y, y + 1]
        x_range = [x - 1, x, x + 1]
        neighbours = list()
        for row in y_range:
            for col in x_range:
                if (x != col or y != row) and self.is_on_board(col, row):
                    neighbours.append(self.cell(col, row))
        return neighbours
