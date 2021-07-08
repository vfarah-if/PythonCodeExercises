from game_of_life.cell import Cell
from game_of_life.cell_state import CellState


class TestCellShould:

    def test_initialise_by_default_as_a_dead(self):
        cell = Cell()

        assert cell is not None
        assert cell.current_state is CellState.Dead

    def test_come_to_life_when_three_live_neighbours_cause_reproduction(self, dead_cell):
        dead_cell.add_neighbour(Cell(CellState.Alive))
        dead_cell.add_neighbour(Cell(CellState.Alive))
        dead_cell.add_neighbour(Cell(CellState.Alive))

        assert dead_cell.next_state() is CellState.Alive

    def test_killing_live_cell_when_fewer_than_two_live_neighbours_cause_underpopulation(self, living_cell):
        living_cell.add_neighbour(Cell(CellState.Dead))
        living_cell.add_neighbour(Cell(CellState.Dead))
        living_cell.add_neighbour(Cell(CellState.Dead))

        assert living_cell.next_state() is CellState.Dead

    def test_live_cell_with_two_live_neighbours_stays_alive_by_thriving_in_ideal_conditions(self, living_cell):
        living_cell.add_neighbour(Cell(CellState.Alive))
        living_cell.add_neighbour(Cell(CellState.Alive))
        living_cell.add_neighbour(Cell(CellState.Dead))

        assert living_cell.next_state() is CellState.Alive

    def test_more_than_three_live_neighbours_kills_live_cell_by_virtue_of_over_population(self, living_cell):
        living_cell.add_neighbour(Cell(CellState.Alive))
        living_cell.add_neighbour(Cell(CellState.Alive))
        living_cell.add_neighbour(Cell(CellState.Alive))
        living_cell.add_neighbour(Cell(CellState.Alive))

        assert living_cell.next_state() is CellState.Dead

    def test_should_visualise_cell_by_status(self, living_cell):

        assert str(living_cell) == 'X'

        living_cell.current_state = CellState.Dead
        assert str(living_cell) == ' '
