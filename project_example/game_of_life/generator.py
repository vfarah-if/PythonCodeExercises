from game_of_life.cell import Cell


class Generator:
    """Game of life generator"""
    def __init__(self, size: int):
        self.size = size
        self.board = list()
        self.initialise_board()

    def initialise_board(self):
        for y in range(self.size):
            col = list()
            for x in range(self.size):
                col.append(Cell())
            self.board.append(col)

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
