def strategy_calculate(opponent_shape, strategy):
    opponent_shapes = {"A": 1, "B": 2, "C": 3}  # R, P, S
    shapes = ["A", "C", "B"]  # R S P
    if strategy == "Y":  # draw
        return opponent_shapes[opponent_shape] + 3
    elif strategy == "Z":  # win strategy
        player_shape = shapes[shapes.index(opponent_shape) - 1]
        return opponent_shapes[player_shape] + 6
    else:
        player_shape = shapes[shapes.index(opponent_shape) - 2]
        return opponent_shapes[player_shape]


def run_guide():
    with open("input.txt", "r") as f:
        total = 0
        while line := f.readline().strip():
            shapes = line.split(' ')
            total += strategy_calculate(*shapes)
        print(total)


if __name__ == "__main__":
    run_guide()
