from game_of_life.cell import Cell


class Generator:
    def __init__(self, size: int):
        self.size = size
        self.board = list()
        for y in range(size):
            col = list()
            for x in range(size):
                col.append(Cell())
            self.board.append(col)

    def __str__(self):
        result = ' | '
        for y in range(self.size):
            if y != 0:
                result += '\n | '
            for x in range(self.size):
                item = str(self.board[x][y])
                result += f'{item} | '
        return result
