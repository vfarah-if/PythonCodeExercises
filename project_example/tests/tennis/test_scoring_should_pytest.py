
import pytest


def tennisScore(playerOneScore: int, playerTwoScore: int):
    scoreNames = ["Love", "Fifteen", "Thirty"]
    return scoreNames[playerOneScore]+"-All"


@pytest.mark.parametrize("playerOneScore, playerTwoScore, expectedResult",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          ])
def test_scoring(playerOneScore: int, playerTwoScore: int, expectedResult: str):
    actualScore = tennisScore(playerOneScore, playerTwoScore)
    assert actualScore == expectedResult


# def test_0_0_love_all():
#     actual = tennisScore(0, 0)
#     assert actual == "Love-All"


# def test_1_1_fifteen_all():
#     actual = tennisScore(1, 1)
#     assert actual == "Fifteen-All"
