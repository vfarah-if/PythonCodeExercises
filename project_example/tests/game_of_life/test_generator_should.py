from game_of_life.generator import Generator
from os import linesep


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
