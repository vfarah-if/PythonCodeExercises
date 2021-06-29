from game_of_life.cell import Cell


class TestCellShould:

    def test_initialise_by_default_as_a_dead(self):
        cell = Cell()

        assert cell is not None
        assert not cell.is_alive

    def test_come_to_life_when_three_live_neighbours_cause_reproduction(self):
        cell = Cell()
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))

        cell.re_generate()

        cell.is_alive is True

    def test_killing_live_cell_when_fewer_than_two_live_neighbours_case_underpopulation(self):
        cell = Cell(True)
        cell.add_neighbour(Cell(False))
        cell.add_neighbour(Cell(False))
        cell.add_neighbour(Cell(False))
        assert cell.is_alive is True

        cell.re_generate()

        assert not cell.is_alive

    def test_live_cell_with_two_live_neighbours_stays_alive_for_next_generation(self):
        cell = Cell(True)
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(False))
        assert cell.is_alive is True

        cell.re_generate()

        assert cell.is_alive

    def test_more_than_three_live_neighbours_kills_live_cell_by_virtue_of_over_population(self):
        cell = Cell(True)
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))
        cell.add_neighbour(Cell(True))

        cell.re_generate()

        assert not cell.is_alive

    def test_should_visualise_cell_by_status(self):
        cell = Cell(True)

        assert str(cell) == 'X'

        cell.is_alive = False
        assert str(cell) == ' '
