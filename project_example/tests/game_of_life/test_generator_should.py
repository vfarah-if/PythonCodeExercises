from game_of_life.generator import Generator
from os import linesep


class TestGeneratorShould:
    def test_should_generate_a_five_by_five_empty_board(self):
        generator = Generator(5)

        assert str(generator) == (
            f" |   |   |   |   |   | {linesep}"            
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | {linesep}"
            f" |   |   |   |   |   | "
        )
