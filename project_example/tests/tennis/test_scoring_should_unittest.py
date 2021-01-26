from _pytest.mark.structures import ParameterSet
from tennis.scoring import tennisScore
from unittest import TestCase


class TennisScoringShould(TestCase):

    def test_score(self):
        testCases = [
            (0, 0, "Love-All"),
            (1, 1, "Fifteen-All"),
            (2, 2, "Thirty-All"),
            (3, 3, "Forty-All"),
            (1, 0, "Advantage Player 1"),
        ]
        for playerOnePoints, playerTwoPoints, expectedResult in testCases:
            with self.subTest(f"{playerOnePoints}{playerTwoPoints} -> {expectedResult}"):
                self.assertEqual(
                    tennisScore(playerOnePoints, playerTwoPoints),
                    expectedResult)
