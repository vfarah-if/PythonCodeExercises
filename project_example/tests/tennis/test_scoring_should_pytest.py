
def tennisScore(playerOneScore: int, playerTwoScore: int):
    if playerOneScore == 0 and playerTwoScore == 0:
        return "Love-All"
    elif playerOneScore == 1 and playerTwoScore == 1:
        return "Fifteen-All" 


def test_0_0_love_all():
    actual = tennisScore(0, 0)
    assert actual == "Love-All"


def test_1_1_fifteen_all():
    actual = tennisScore(1, 1)
    assert actual == "Fifteen-All"
