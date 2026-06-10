high_score_board = []

def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Record player scores, calculate total, and determine rank.

    *args:
        scores: Variable number of round scores.
    **kwargs:
        bonus: Optional points added to total.
        multiplier: Optional multiplier applied at the end.
    """
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")
    
    for score in scores:
        if score < 0:
            return (player, 0, 0, "negative score not allowed")
    
    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)
    
    high_score_board.append((player, total))
    high_score_board.sort(key=lambda item: item[1], reverse=True)
    
    current_rank = 1
    for index, (p_name, p_score) in enumerate(high_score_board):
        if p_name == player and p_score == total:
            current_rank = index + 1
            break
            
    if current_rank == 1:
        status = "high score!"
    else:
        status = f"rank {current_rank}"
        
    return (player, rounds, total, status)

print(record_game("Ali", 10, 20, 30, bonus=5, multiplier=1.5))
print(record_game("Fahad", 40, 50, bonus=10))
print(record_game("Noor", 15, 25, 35, multiplier=2.0))
print(record_game("Khaled"))

print("\nFinal Leaderboard:")
print(high_score_board)
