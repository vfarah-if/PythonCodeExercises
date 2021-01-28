from tennis.scoring import tennis_score
from unittest import TestCase


class TennisScoringShould(TestCase):

    def test_score(self):
        test_cases = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            (3, 3, "Forty-All"),
            (1, 0, "Fifteen-Love"),
            (0, 1, "Love-Fifteen"),

        ]
        for player_one_points, player_two_points, expected_result in test_cases:
            with self.subTest(f"{player_one_points}{player_two_points} -> {expected_result}"):
                self.assertEqual(
                    tennis_score(player_one_points, player_two_points),
                    expected_result)
