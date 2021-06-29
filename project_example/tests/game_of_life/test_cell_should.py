from game_of_life.cell import Cell


class TestCellShould:

    def test_initialise_by_default_as_a_dead_cell_storing_the_position(self):
        cell = Cell(0, 1)

        assert cell is not None
        assert not cell.is_alive
        assert cell.x == 0
        assert cell.y == 1

    def test_come_to_life_when_three_live_neighbours_cause_reproduction(self):
        cell = Cell(0, 1)
        cell.neighbours.append(Cell(0, 0, True))
        cell.neighbours.append(Cell(0, 2, True))
        cell.neighbours.append(Cell(1, 1, True))

        cell.re_generate()

        cell.is_alive is True
