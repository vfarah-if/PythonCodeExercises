def tennisScore(playerOneScore: int, playerTwoScore: int):
    scoreNames = ["Love", "Fifteen", "Thirty", "Forty"]
    if playerOneScore == playerTwoScore:
        return scoreNames[playerOneScore]+"-All"
