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

    def test_killing_live_cell_when_fewer_than_two_live_neighbours_case_underpopulation(self):
        cell = Cell(0, 1, True)
        cell.neighbours.append(Cell(0, 0, False))
        cell.neighbours.append(Cell(0, 2, False))
        cell.neighbours.append(Cell(1, 1, False))
        assert cell.is_alive is True

        cell.re_generate()

        assert not cell.is_alive

    def test_live_cell_with_two_live_neighbours_stays_alive_for_next_generation(self):
        cell = Cell(0, 1, True)
        cell.neighbours.append(Cell(0, 0, True))
        cell.neighbours.append(Cell(0, 2, True))
        cell.neighbours.append(Cell(1, 1, False))
        assert cell.is_alive is True

        cell.re_generate()

        assert cell.is_alive

    def test_more_than_three_live_neighbours_kills_live_cell_by_virtue_of_over_population(self):
        cell = Cell(0, 1, True)
        cell.neighbours.append(Cell(0, 0, True))
        cell.neighbours.append(Cell(0, 2, True))
        cell.neighbours.append(Cell(1, 0, True))
        cell.neighbours.append(Cell(1, 1, True))

        cell.re_generate()

        assert not cell.is_alive
