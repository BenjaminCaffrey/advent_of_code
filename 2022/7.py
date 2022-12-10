from __future__ import annotations
from typing import Optional, Dict

class FileSystemObject:
    def __init__(self, name: str, size: Optional[int] = None, parent: FileSystemObject = None, depth: int = 0):
        self.name: str = name
        self.size: Optional[int] = size
        self.parent: Optional[FileSystemObject] = parent
        self.children: Dict[str, FileSystemObject] = {}
        self.depth: int = depth

    def __repr__(self):
        return '\n' + str({'name': self.name, 'size': self.size, 'children': self.children})

    def populate(self, input_line: str):
        s1, name = input_line.strip().split(' ')
        if s1 == 'dir':
            self.children[name] = FileSystemObject(name = name, parent = self, depth = (self.depth + 1))
        else:
            self.children[name] = FileSystemObject(name = name, size = int(s1), parent = self, depth = (self.depth + 1))


def calculate_all_sizes(cur_dir: FileSystemObject):
    cur_size = 0
    for child in cur_dir.children.values():
        if not child.size:
            calculate_all_sizes(child)
        
        if child.size:
            cur_size += child.size
    
    cur_dir.size = cur_size

def sum_folder_sizes(cur_dir: FileSystemObject):
    cur_sum = 0
    if cur_dir.size:
        if cur_dir.size <= 100_000 and cur_dir.children:
            cur_sum += cur_dir.size

        for child in cur_dir.children.values():
            cur_sum += sum_folder_sizes(child)

        return cur_sum

def find_best_dir_size(cur_dir: FileSystemObject, cur_best: int, space_needed: int):
    if cur_dir.size:
        if cur_dir.size >= space_needed and cur_dir.size <= cur_best:
            cur_best = cur_dir.size
        for child in cur_dir.children.values():
            cur_best = find_best_dir_size(child, cur_best, space_needed)
        return cur_best

def parse_input() -> FileSystemObject:
    root_dir = FileSystemObject(name = "/")
    cur_dir = root_dir

    with open("7-input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            if line == '$ cd /':
                continue
            
            if not line.startswith('$'):
                cur_dir.populate(line)
            elif line == '$ cd ..':
                if cur_dir.parent:
                    cur_dir = cur_dir.parent
            elif line.startswith('$ cd'):
                destination_dir_name = line.split(' ')[2]
                cur_dir = cur_dir.children[destination_dir_name]
            
    return root_dir


if __name__ == "__main__":
    root_dir = parse_input()
    calculate_all_sizes(root_dir)

    print(sum_folder_sizes(root_dir))

    if root_dir.size:
        total_disk_size = 70_000_000
        space_for_update = 30_000_000
        cur_free_space = total_disk_size - root_dir.size
        space_needed = space_for_update - cur_free_space 

        print(f"{cur_free_space=}")
        print(f"{space_needed=}")

        best_dir_size = find_best_dir_size(root_dir, root_dir.size, space_needed)
        print(best_dir_size)