def tennis_score(player_one_score: int, player_two_score: int):
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]
    if player_one_score == player_two_score:
        return score_names[player_one_score] + "-All"
    else:
        return f"{score_names[player_one_score]}-{score_names[player_two_score]}"
