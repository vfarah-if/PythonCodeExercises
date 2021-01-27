
from tennis.scoring import tennis_score
import pytest


@pytest.mark.parametrize("playerOneScore, playerTwoScore, expectedResult",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (3, 3, "Forty-All"),
                          (1, 0, "Fifteen-Love"),
                          (0, 1, "Love-Fifteen"),
                          ])
def test_scoring(playerOneScore: int, playerTwoScore: int, expectedResult: str):
    actualScore = tennis_score(playerOneScore, playerTwoScore)
    assert actualScore == expectedResult
