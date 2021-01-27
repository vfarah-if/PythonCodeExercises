def tennis_score(playerOneScore: int, playerTwoScore: int):
    scoreNames = ["Love", "Fifteen", "Thirty", "Forty"]
    if playerOneScore == playerTwoScore:
        return scoreNames[playerOneScore]+"-All"
    else:
        return f"{scoreNames[playerOneScore]}-{scoreNames[playerTwoScore]}"
