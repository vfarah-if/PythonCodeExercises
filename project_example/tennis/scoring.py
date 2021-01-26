def tennisScore(playerOneScore: int, playerTwoScore: int):
    leader = "Player 1"
    scoreNames = ["Love", "Fifteen", "Thirty", "Forty"]
    if playerTwoScore > playerOneScore:
        leader = "Player 2"
    if playerOneScore == playerTwoScore:
        return scoreNames[playerOneScore]+"-All"
    else:
        return f"Advantage {leader}"
