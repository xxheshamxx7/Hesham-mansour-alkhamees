high_score_board = []  

def record_game(player, *scores, bonus=0, multiplier=1.0):
    """
    Record a game for a player.

    Parameters:
        player (str): Player name (positional argument).
        *scores: Variable number of round scores.
        bonus (int, optional): Extra points added to raw total. Default 0.
        multiplier (float, optional): Multiplier applied after bonus. Default 1.0.

    Returns:
        tuple: (player, rounds, total, status)
            - player: name
            - rounds: number of valid scores
            - total: final score (int)
            - status: "no rounds played", "negative score not allowed",
                    "high score!", or "rank N"

    Rules:
        - If no scores provided -> (player, 0, 0, "no rounds played")
        - If any negative score -> (player, 0, 0, "negative score not allowed")
        - Otherwise:
            raw_total = sum(scores)
            total = int((raw_total + bonus) * multiplier)
            rounds = len(scores)
            Append (player, total) to global high_score_board
            Determine rank by sorting board descending by total:
                rank 1 -> status = "high score!"
                else   -> status = f"rank {rank}"
    """
    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")
    
    if any(s < 0 for s in scores):
        return (player, 0, 0, "negative score not allowed")
    
    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)
    
    high_score_board.append((player, total))
    
    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)
    rank = 1
    for i, (p, t) in enumerate(sorted_board, start=1):
        if p == player and t == total:
            rank = i
            break
    
    status = "high score!" if rank == 1 else f"rank {rank}"
    return (player, rounds, total, status)


if __name__ == "__main__":
    high_score_board.clear()
    
    print(record_game("ahmad", 10, 20, 30, bonus=5, multiplier=1.2))
    print(record_game("mohammad", 15, -5, 25))   
    print(record_game("saad", 40, 50, bonus=10))
    print(record_game("sara",))            
    print(record_game("nora", 100, 200, bonus=0, multiplier=0.5))
    
    print("\nFinal Leaderboard:")
    for rank, (player, total) in enumerate(sorted(high_score_board, key=lambda x: x[1], reverse=True), start=1):
        print(f"{rank}. {player}: {total}")