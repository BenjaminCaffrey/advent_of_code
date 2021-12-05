from typing import List, Tuple, Dict
from collections import defaultdict


class P:
    def __init__(self, tuple: Tuple[int, int]):
        self.x = tuple[0]
        self.y = tuple[1]

    def __str__(self):
        return f"({self.x},{self.y})"


class VentLine:
    def __init__(self, p1: P, p2: P):
        self.p1 = p1
        self.p2 = p2

    def mark_dangerous_points(
        self, grid: Dict[Tuple[int, int], int], count_diagonal: bool
    ) -> None:
        # print(f"p1: {self.p1}, p2: {self.p2}")
        if self.p1.x == self.p2.x:
            for y in range(min(self.p1.y, self.p2.y), max(self.p1.y, self.p2.y) + 1):
                # print(f"Marking point {self.p1.x, y}")
                grid[(self.p1.x, y)] += 1
        elif self.p1.y == self.p2.y:
            for x in range(min(self.p1.x, self.p2.x), max(self.p1.x, self.p2.x) + 1):
                # print(f"Marking point {x, self.p1.y}")
                grid[(x, self.p1.y)] += 1
        elif count_diagonal:
            num_points = abs(self.p1.x - self.p2.x) + 1
            x_direction = 1 if self.p1.x < self.p2.x else -1
            y_direction = 1 if self.p1.y < self.p2.y else -1
            for i in range(num_points):
                # print(
                #     f"Marking point {(self.p1.x + (i * x_direction), self.p1.y + (i * y_direction))}"
                # )
                grid[
                    (self.p1.x + (i * x_direction), self.p1.y + (i * y_direction))
                ] += 1


def get_num_dangerous_points(
    vent_lines: List[VentLine], count_diagonal: bool = False
) -> int:
    # danger_grid is a dictionary with keys represnting point coordinates
    # and values representing the number of hydrothermal vents at that point
    danger_grid: Dict[Tuple[int, int], int] = defaultdict(int)
    for vent_line in vent_lines:
        vent_line.mark_dangerous_points(danger_grid, count_diagonal)
    # print(danger_grid)
    return len([value for value in danger_grid.values() if value > 1])


def _parse_input(filename: str) -> List[VentLine]:
    vent_lines = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            p1_str, p2_str = line.split(" -> ")
            p1_x, p1_y = [int(x) for x in p1_str.split(",")]
            p2_x, p2_y = [int(x) for x in p2_str.split(",")]
            p1 = P((p1_x, p1_y))
            p2 = P((p2_x, p2_y))
            vent_lines.append(VentLine(p1, p2))
    return vent_lines


if __name__ == "__main__":
    vent_lines = _parse_input("5-input-example.txt")
    num_dangerous_points = get_num_dangerous_points(vent_lines)
    assert num_dangerous_points == 5

    vent_lines = _parse_input("5-input.txt")
    num_dangerous_points = get_num_dangerous_points(vent_lines)
    print(num_dangerous_points)

    vent_lines = _parse_input("5-input-example.txt")
    num_dangerous_points = get_num_dangerous_points(vent_lines, count_diagonal=True)
    assert num_dangerous_points == 12

    vent_lines = _parse_input("5-input.txt")
    num_dangerous_points = get_num_dangerous_points(vent_lines, count_diagonal=True)
    print(num_dangerous_points)
