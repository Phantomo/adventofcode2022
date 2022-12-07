class Directory:
    def __init__(self, name):
        self.name = name
        self.children = dict()
        self.parent = None
        self.files = dict()

    def add_file(self, size, name):
        if name not in self.files.keys():
            self.files[name] = size

    def count_size(self):
        size = sum([file_size for file_size in self.files.values()])
        for child in self.children.values():
            size += child.count_size()
        return size

    def count_small_directory_size(self):
        size = sum([file_size for file_size in self.files.values()])
        for child in self.children.values():
            child_count = child.count_small_directory_size()
            if child_count < 100000:
                size += child_count
        return size if size < 100000 else 0

    def sum_small_directory(self):
        return sum([self])

    def add_child(self, name, children):
        if name not in self.children.keys():
            self.children[name] = children

    def get_child(self, name):
        return self.children[name]

    def return_all_directories_list(self):
        directories = []
        self._get_directories(self, directories)
        return directories

    def _get_directories(self, head, directories):
        if head is not None:
            if head not in directories:
                directories.append(head)
            for d in head.children.values():
                self._get_directories(d, directories)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

def scan_file_system(data):
    core = Directory("/")
    current_directory = core
    for line in data[1:]:
        line = line.strip('\n')
        if line.startswith("$"):
            line = line.lstrip("$ ")
            if line == "cd ..":
                current_directory = current_directory.parent
            elif line == "ls":
                pass
            elif line.startswith("cd"):
                directory = line.split(" ")
                current_directory = current_directory.get_child(directory[1])
        else:
            contents = line.split(" ")
            if contents[0] == "dir":
                new_dir = Directory(contents[1])
                current_directory.add_child(new_dir.name, new_dir)
                new_dir.parent = current_directory
            else:
                current_directory.add_file(int(contents[0]), contents[1])
    return core


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    file_system = scan_file_system(data)

    directories = file_system.return_all_directories_list()
    need_to_free_space = 30_000_000 - (70_000_000 - file_system.count_size())
    max_size = file_system.count_size()
    for d in directories:
        dir_size = d.count_size()
        if need_to_free_space < dir_size < max_size:
            max_size = dir_size
    print(max_size)


if __name__ == "__main__":
    main()
