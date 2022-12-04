def range_overlaps(line):
    ranges = line.split(',')
    ranges = [list(map(int, _range.split('-'))) for _range in ranges]
    if ranges[0][1] - ranges[0][0] >= ranges[1][1] - ranges[1][0]:
        if ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]:
            return 1
    elif ranges[1][0] <= ranges[0][0] and ranges[1][1] >= ranges[0][1]:
        return 1
    return 0


def main():
    with open("input.txt", "r") as f:
        total = 0
        while line := f.readline().strip():
            total += range_overlaps(line)
        print(total)


if __name__ == "__main__":
    main()
