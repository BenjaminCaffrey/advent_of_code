from typing import List, Dict, Tuple
from math import prod


class P:
    def __init__(self, r: int, c: int, val: int):
        self.r = r
        self.c = c
        self.val = val


def find_low_spots(height_map: List[List[int]]) -> List[P]:
    low_spots = []
    max_row = len(height_map)
    max_col = len(height_map[0])
    for r, row in enumerate(height_map):
        # print(row)
        for c, val in enumerate(row):
            # print(f"Checking spot {r,c} with value {val}")

            # Check left
            if (c > 0) and (height_map[r][c - 1] <= val):
                continue
            # Check up
            if (r > 0) and (height_map[r - 1][c] <= val):
                continue

            # Check right
            if (c < max_col - 1) and (height_map[r][c + 1] <= val):
                continue

            # Check below
            if (r < max_row - 1) and (height_map[r + 1][c] <= val):
                continue

            # print(f"Found a low spot {r,c} with value {val}")
            low_spots.append(P(r, c, val))
    return low_spots


def get_basin_size(p: P, height_map: List[List[int]]) -> int:
    seen_points = {(p.r, p.c): True}
    recursive_dfs(p.r, p.c, seen_points, height_map)
    return len(seen_points.values())


def recursive_dfs(
    r: int,
    c: int,
    seen_points: Dict[Tuple[int, int], bool],
    height_map: List[List[int]],
) -> None:
    max_row = len(height_map)
    max_col = len(height_map[0])
    seen_points[(r, c)] = True
    # print("Recursing! Seen points:")
    # print(seen_points)
    # print(f"cur_point: {r,c}")
    # print("")
    # Check left
    if (c > 0) and (height_map[r][c - 1] != 9):
        if not seen_points.get((r, c - 1), False):
            recursive_dfs(r, c - 1, seen_points, height_map)
    # Check up
    if (r > 0) and (height_map[r - 1][c] != 9):
        if not seen_points.get((r - 1, c), False):
            recursive_dfs(r - 1, c, seen_points, height_map)

    # Check right
    if (c < max_col - 1) and (height_map[r][c + 1] != 9):
        if not seen_points.get((r, c + 1), False):
            recursive_dfs(r, c + 1, seen_points, height_map)

    # Check below
    if (r < max_row - 1) and (height_map[r + 1][c] != 9):
        if not seen_points.get((r + 1, c), False):
            recursive_dfs(r + 1, c, seen_points, height_map)


def _parse_input(filename: str) -> List[List[int]]:
    height_map = []
    with open(filename) as f:
        for line in f.readlines():
            row = [int(x) for x in list(line.strip())]
            height_map.append(row)
    return height_map


if __name__ == "__main__":
    # Parse inputs
    example_height_map = _parse_input("9-input-example.txt")
    height_map = _parse_input("9-input.txt")

    # Part 1
    low_spots = find_low_spots(example_height_map)
    low_spot_vals = [x.val for x in low_spots]
    risk_level = sum(low_spot_vals) + len(low_spots)
    assert risk_level == 15

    low_spots = find_low_spots(height_map)
    low_spot_vals = [x.val for x in low_spots]
    risk_level = sum(low_spot_vals) + len(low_spots)
    print(risk_level)

    # Part 2
    low_spots = find_low_spots(example_height_map)
    basin_sizes = []
    for low_spot in low_spots:
        basin_size = get_basin_size(low_spot, example_height_map)
        basin_sizes.append(basin_size)
    assert prod(sorted(basin_sizes)[-3:]) == 1134

    low_spots = find_low_spots(height_map)
    basin_sizes = []
    for low_spot in low_spots:
        basin_size = get_basin_size(low_spot, height_map)
        basin_sizes.append(basin_size)
    print(prod(sorted(basin_sizes)[-3:]))
