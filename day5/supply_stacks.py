def clean_movement_string(line):
    return line.replace("move", "").replace("from", "").replace("to", "").strip(" ").split("  ")


def parse_supply_input(data):
    divided_parts = data.split("\n\n")
    moves = divided_parts[1]
    cargo_input = [column for column in divided_parts[0].split('\n')]
    stacks = {int(stack): [] for stack in cargo_input.pop(-1).strip(" ").split("   ")}
    for cargo in reversed(cargo_input):
        # an = a1 + d(n-1) | d = 4
        index = 1
        position = 1
        while index < len(cargo):
            if cargo[index] != " ":
                stacks[position].append(cargo[index])
            position += 1
            index = 1 + 4 * (position - 1)

    return stacks, [list(map(int, clean_movement_string(move))) for move in moves.split('\n')]


def main():
    with open("input.txt", "r") as f:
        data = f.read()
    stacks, moves = parse_supply_input(data)
    for move in moves:
        stacks[move[2]].extend(reversed(stacks[move[1]][-move[0]:]))
        del stacks[move[1]][-move[0]:]

    result = []
    for i in range(1, len(stacks) + 1):
        if stacks[i]:
            result.append(stacks[i].pop(-1))
    print("".join(last_cargo for last_cargo in result))


if __name__ == "__main__":
    main()