high_score_board = []


def record_game(player, *scores, bonus=0, multiplier=1.0):

    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")

    for score in scores:
        if score < 0:
            return (player, 0, 0, "negative score not allowed")

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    high_score_board.append((player, total))

    sorted_board = sorted(
        high_score_board,
        key=lambda item: item[1],
        reverse=True
    )
    rank = 0
    for i, item in enumerate(sorted_board, start=1):
        if item[0] == player and item[1] == total:
            rank = i
            break

    if rank == 1:
        status = "high score!"
    else:
        status = f"rank {rank}"

    return (player, rounds, total, status)



print(record_game("Ali", 10, 20, 30))
print(record_game("Sara", 50, 40))
print(record_game("Omar", 25, 25, 25, bonus=10))
print(record_game("Fahad"))
print(record_game("Khalid", 10, -5, 20))

print("Final Leaderboard:")
print(high_score_board)