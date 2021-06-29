from _pytest.python_api import raises
from os import linesep

from game_of_life.generator import Generator


class TestGeneratorShould:
    def test_generate_a_five_by_five_empty_board(self):
        generator = Generator(5)

        assert str(generator) == (
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | "
        )

    def test_generate_a_five_by_five_with_seeded_data(self):
        generator = Generator(5, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                                  (0, 1)
                                  ])

        assert str(generator) == (
            f" | X | X | X | X | X | {linesep}"
            f" | X |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | "
        )

    def test_generate_one_by_one_throws_an_attribute_error(self):
        with raises(AttributeError):
            Generator(1, [])

    def test_generate_a_two_by_two_with_three_neighbours_always_should_stay_alive_after_tick(self):
        generator = Generator(2, [
            (0, 0), (1, 0),
            (0, 1), (1, 1),
        ])

        assert str(generator) == (
            f" | X | X | {linesep}"
            f" | X | X | "
        )

        generator.tick()

        assert str(generator) == (
            f" | X | X | {linesep}"
            f" | X | X | "
        )

    def test_generate_a_four_by_four_block_still_life(self):
        generator = Generator(4, [
            (1, 1), (2, 1),
            (1, 2), (2, 2),
        ])

        assert str(generator) == (
            f" |   |   |   |   | {linesep}"
            f" |   | X | X |   | {linesep}"
            f" |   | X | X |   | {linesep}"
            f" |   |   |   |   | "
        )

        generator.tick()

        assert str(generator) == (
            f" |   |   |   |   | {linesep}"
            f" |   | X | X |   | {linesep}"
            f" |   | X | X |   | {linesep}"
            f" |   |   |   |   | "
        )
