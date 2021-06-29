from game_of_life.cell import Cell


class Generator:
    """Game of life generator"""
    def __init__(self, size: int, seed_data: list):
        """
        Constructor
        @param size: Board Size or matrix setting for x and y
        @param seed_data: List of tuples and teh tuple denoting x and y
        """
        self.size = size
        self.board = list()
        self._initialise_board()
        self._seed(seed_data)

    def _initialise_board(self):
        for y in range(self.size):
            col = list()
            for x in range(self.size):
                col.append(Cell())
            self.board.append(col)

    def _seed(self, positions: list):
        for item in positions:
            x = item[0]
            y = item[1]
            cell = self.board[x][y]
            if cell is not None:
                cell.is_alive = True

    def __str__(self):
        return self.picture_board()

    def picture_board(self):
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += '\n | '
            for x in range(self.size):
                item = str(self.board[x][y])
                result += f'{item} | '
        return result
