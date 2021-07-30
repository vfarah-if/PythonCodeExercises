from pytest import fixture

from game_of_life.cell import Cell
from game_of_life.cell_state import CellState


@fixture
def living_cell() -> Cell:
    return Cell(CellState.Alive)


@fixture
def dead_cell() -> Cell:
    return Cell()
