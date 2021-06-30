from pytest import fixture

from game_of_life.cell import Cell
from game_of_life.cell_state import CellState


@fixture
def living_cell() -> Cell:
    """
    @return: Alive Cell
    """
    return Cell(0, 0, CellState.Alive)


@fixture
def dead_cell() -> Cell:
    """
    @return: Dead Cell
    """
    return Cell(0, 0)
