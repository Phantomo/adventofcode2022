def strategy_calculate(opponent_shape, player_shape):
    opponent_shapes = {"A": 1, "B": 2, "C": 3}
    player_shapes = {"X": 1, "Y": 2, "Z": 3}
    score = player_shapes[player_shape]
    if opponent_shapes[opponent_shape] == player_shapes[player_shape]:
        score += 3
    elif player_shapes[player_shape] - 1 == opponent_shapes[opponent_shape] or player_shapes[player_shape] + 2 == opponent_shapes[opponent_shape]:
        score += 6
    return score


def run_guide():
    with open("input.txt", "r") as f:
        total = 0
        while line := f.readline().strip():
            shapes = line.split(' ')
            total += strategy_calculate(*shapes)
        print(total)

if __name__ == "__main__":
    run_guide()