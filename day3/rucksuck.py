def calculate_rucksuck(line):
    line_length = len(line)
    compartment1 = line[:line_length//2]
    compartment2 = line[line_length//2:line_length]
    for item in compartment1:
        for item2 in compartment2:
            if item == item2:
                return ord(item) - 96 if item.islower() else ord(item) - 38


def main():
    with open("input.txt", "r") as f:
        total = 0
        while line := f.readline().strip():
            total += calculate_rucksuck(line)
        print(total)

if __name__ == "__main__":
    main()
