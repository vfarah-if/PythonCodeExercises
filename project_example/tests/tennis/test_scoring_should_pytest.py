
def tennisScore(playerOneScore: int, playerTwoScore: int):
    if playerOneScore == 0 and playerTwoScore == 0:
        return "Love-All"


def test_0_0_love_all():
    actual = tennisScore(0, 0)
    assert actual == "Love-All"

