def calculate_rucksuck(line):
    line_length = len(line)
    compartment1 = line[:line_length//2]
    compartment2 = line[line_length//2:line_length]
    for item in compartment1:
        for item2 in compartment2:
            if item == item2:
                return ord(item) - 96 if item.islower() else ord(item) - 38


def calculate_group_rucksuck(lines):
    for item in lines[0]:
        for item2 in lines[1]:
            for item3 in lines[2]:
                if item == item2 == item3:
                    return ord(item) - 96 if item.islower() else ord(item) - 38

def main():
    with open("input.txt", "r") as f:
        total = 0
        try:
            while f:
                lines = [next(f) for x in range(3)]
                total += calculate_group_rucksuck(lines)
        except StopIteration:
            print(total)

if __name__ == "__main__":
    main()
