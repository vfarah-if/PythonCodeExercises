from game_of_life.cell import Cell


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
        for y in range(self.size):
            for x in range(self.size):
                cell = self.board[x][y]
                cell.re_generate()

    def _initialise_board(self):
        for y in range(self.size):
            col = list()
            for x in range(self.size):
                col.append(Cell())
            self.board.append(col)

    def _initialise_neighbours(self):
        for y in range(self.size):
            for x in range(self.size):
                above_y = y - 1
                left_of_x = x - 1
                right_of_x = x + 1
                below_y = y + 1
                current_cell = self.board[x][y]
                # rotate around the current cell linearly
                # top left diagonal
                if above_y >= 0 and left_of_x > 0:
                    neighbour = self.board[left_of_x][above_y]
                    current_cell.add_neighbour(neighbour)
                # top middle
                if above_y >= 0:
                    neighbour = self.board[x][above_y]
                    current_cell.add_neighbour(neighbour)
                # top right diagonal
                if above_y >= 0 and right_of_x < self.size:
                    neighbour = self.board[right_of_x][above_y]
                    current_cell.add_neighbour(neighbour)
                # right
                if right_of_x < self.size:
                    neighbour = self.board[right_of_x][y]
                    current_cell.add_neighbour(neighbour)
                # bottom right diagonal
                if below_y < self.size and right_of_x < self.size:
                    neighbour = self.board[right_of_x][below_y]
                    current_cell.add_neighbour(neighbour)
                # bottom middle
                if below_y < self.size:
                    neighbour = self.board[x][below_y]
                    current_cell.add_neighbour(neighbour)
                # bottom left diagonal
                if below_y < self.size and left_of_x >= 0:
                    neighbour = self.board[left_of_x][below_y]
                    current_cell.add_neighbour(neighbour)
                # left
                if left_of_x >= 0:
                    neighbour = self.board[left_of_x][y]
                    current_cell.add_neighbour(neighbour)

    def _seed(self, positions: list):
        for item in positions:
            x = item[0]
            y = item[1]
            cell = self.board[x][y]
            if cell is not None:
                cell.is_alive = True

    def __str__(self):
        return self._picture_board()

    def _picture_board(self):
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += '\n | '
            for x in range(self.size):
                item = str(self.board[x][y])
                result += f'{item} | '
        return result
