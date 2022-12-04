# class Range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def overlap(self, range_obj):
#         range()
#         return True



def range_overlaps(line):
    ranges = line.split(',')
    ranges = [list(map(int, _range.split('-'))) for _range in ranges]
    if set(range(ranges[0][0], ranges[0][1] + 1)).intersection(range(ranges[1][0], ranges[1][1]+1)):
        return True
    return False


def main():
    with open("input.txt", "r") as f:
        total = 0
        while line := f.readline().strip():
            if range_overlaps(line):
                total += 1
        print(total)


if __name__ == "__main__":
    main()
