from game_of_life.cell import Cell


class TestCellShould:

    def test_generate_by_default_as_a_dead_cell(self):
        cell = Cell(0, 1, False)

        assert cell is not None
        assert not cell.is_alive
        assert cell.x == 0
        assert cell.y == 1
