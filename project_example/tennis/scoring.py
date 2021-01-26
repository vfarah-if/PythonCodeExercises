def tennisScore(playerOneScore: int, playerTwoScore: int):
    scoreNames = ["Love", "Fifteen", "Thirty"]
    if playerOneScore == playerTwoScore:
        return scoreNames[playerOneScore]+"-All"
