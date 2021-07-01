from os import linesep

from game_of_life.cell import Cell
from game_of_life.cell_state import CellState


class Generator:
    """Game of life generator"""

    def __init__(self, size: int, seed_data: list = list()):
        """
        Constructor

        @param size: Board Size or matrix setting for x and y and must be minimum 2
        @param seed_data: List of tuples and teh tuple denoting x and y
        """
        if size < 2:
            raise AttributeError('"size" must must be no less than 2', size)
        self.size = size
        self.board = list()
        self._initialise_board()
        self._initialise_neighbours()
        self._seed(seed_data)

    def tick(self):
        """Regenerates all data in the cells generating the patterns from the seeded data"""
        self._calculate_life_expectancy()
        self._regenerate()

    def _regenerate(self):
        for y in range(self.size):
            for x in range(self.size):
                cell = self.get_cell(x, y)
                cell.transfer_state()

    def _calculate_life_expectancy(self):
        for y in range(self.size):
            for x in range(self.size):
                cell = self.get_cell(x, y)
                cell.get_next_state()

    def __str__(self):
        """
        Overrides default string output to represent a simplified visual of what is generated
        @return: Generated visual showing a grid with cells denoting the state
        """
        return self._picture_board()

    def _initialise_board(self):
        for y in range(self.size):
            col = list()
            for x in range(self.size):
                col.append(Cell())
            self.board.append(col)

    def _is_on_board(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def _initialise_neighbours(self):
        for y in range(self.size):
            for x in range(self.size):
                current_cell = self.get_cell(x, y)
                for neighbour in self._get_neighbours(x, y):
                    current_cell.add_neighbour(neighbour)

    def _seed(self, positions: list):
        for item in positions:
            x = item[0]
            y = item[1]
            cell = self.get_cell(x, y)
            if cell is not None:
                cell.current_state = CellState.Alive

    def _picture_board(self):
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += f'{linesep} | '
            for x in range(self.size):
                item = str(self.get_cell(x, y))
                result += f'{item} | '
        return result

    def get_cell(self, x: int, y: int):
        """Get cell on board by position"""
        return self.board[y][x]

    # TODO: Reduce linear logic with algorithm
    def _get_neighbours(self, x, y):
        result = list()
        above_y = y - 1
        left_of_x = x - 1
        right_of_x = x + 1
        below_y = y + 1
        if self._is_on_board(left_of_x, above_y):
            result.append(self.get_cell(left_of_x, above_y))
        if self._is_on_board(x, above_y):
            result.append(self.get_cell(x, above_y))
        if self._is_on_board(right_of_x, above_y):
            result.append(self.get_cell(right_of_x, above_y))
        if self._is_on_board(right_of_x, y):
            result.append(self.get_cell(right_of_x, y))
        if self._is_on_board(right_of_x, below_y):
            result.append(self.get_cell(right_of_x, below_y))
        if self._is_on_board(x, below_y):
            result.append(self.get_cell(x, below_y))
        if self._is_on_board(left_of_x, below_y):
            result.append(self.get_cell(left_of_x, below_y))
        if self._is_on_board(left_of_x, y):
            result.append(self.get_cell(left_of_x, y))
        return result;

