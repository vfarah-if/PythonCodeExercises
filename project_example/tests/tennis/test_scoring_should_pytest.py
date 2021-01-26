
from tennis.scoring import tennisScore
import pytest


@pytest.mark.parametrize("playerOneScore, playerTwoScore, expectedResult",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (3, 3, "Forty-All"),
                          (1, 0, "Advantage Player 1"),
                          ])
def test_scoring(playerOneScore: int, playerTwoScore: int, expectedResult: str):
    actualScore = tennisScore(playerOneScore, playerTwoScore)
    assert actualScore == expectedResult
