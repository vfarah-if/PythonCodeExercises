
from tennis.scoring import tennis_score
import pytest


@pytest.mark.parametrize("player_one_score, player_two_score, expected_result",
                         [(0, 0, "Love-All"),
                          (1, 1, "Fifteen-All"),
                          (2, 2, "Thirty-All"),
                          (3, 3, "Forty-All"),
                          (1, 0, "Fifteen-Love"),
                          (0, 1, "Love-Fifteen"),
                          ])
def test_scoring(player_one_score: int, player_two_score: int, expected_result: str):
    actual_score = tennis_score(player_one_score, player_two_score)
    assert actual_score == expected_result
