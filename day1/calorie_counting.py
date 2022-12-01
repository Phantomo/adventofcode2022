if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        data = f.read()
        calories_group = data.split('\n\n')
        print(max([sum(list(map(int,group.split('\n')))) for group in calories_group]))