def find_first_n_unique(data, n):
    packet = []
    for i, char in enumerate(data, start=1):
        if char in packet:
            del packet[0:packet.index(char)+1]
        packet.append(char)
        if len(packet) == n:
            print(packet)
            return i


def main():
    with open("input.txt", "r") as f:
        data = f.read()
    print(find_first_n_unique(data, 4))


if __name__ == "__main__":
    main()