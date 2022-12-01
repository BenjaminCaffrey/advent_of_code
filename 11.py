import os
from typing import List, Dict, Tuple, Optional
from time import sleep

BLUE = "\033[94m"
RED = "\033[91m"
RESET = "\u001b[0m"


class DumboOctopus:
    def __init__(self, val: int):
        self.val = val

    def __repr__(self) -> str:
        if self.val < 10:
            return str(self.val)
        else:
            return f"{BLUE}X{RESET}"

    def clear(self) -> None:
        if self.val > 9:
            self.val = 0


class DumboOctopusState:
    def __init__(self, octopus_grid: List[List[DumboOctopus]]):
        self.octopus_grid = octopus_grid
        self.step: int = 0
        self.substep: int = 0
        self.total_flashes: int = 0
        self.flashed: Dict[Tuple[int, int], bool] = {}
        self.sync_step: Optional[int] = None

    def __str__(self) -> str:
        os.system("clear")
        output = [f"Current step: {self.step}.{self.substep}"]
        output.extend([f"Total flashes: {self.total_flashes}", "\n"])
        for octopus_row in self.octopus_grid:
            output.append(" ".join([str(x) for x in octopus_row]))
        return "\n".join(output) + "\r"

    def run_n_steps(self, steps: int) -> None:
        for i in range(0, steps):
            self.step += 1
            self.substep = 0
            self.iterate(initial=True)
            self.clear_octopus()

    def run_until_sync(self) -> None:
        while not self.sync_step:
            self.step += 1
            self.substep = 0
            self.iterate(initial=True)
            self.clear_octopus()

    def iterate(self, initial: bool = False) -> None:
        recurse = False
        print(self)
        for r, octopus_row in enumerate(self.octopus_grid):
            for c, dumbo_octopus in enumerate(octopus_row):
                if initial:
                    dumbo_octopus.val += 1
                    recurse = recurse or (dumbo_octopus.val == 10)
                else:
                    if dumbo_octopus.val > 9 and not self.flashed.get((r, c), False):
                        self.flash_octopus(r, c)
                        recurse = True
        sleep(0.3)
        # input("")
        if recurse:
            self.substep += 1
            self.iterate()

    def flash_octopus(self, r: int, c: int) -> None:
        self.total_flashes += 1
        self.flashed[(r, c)] = True
        # Left
        if c > 0:
            octopus = self.octopus_grid[r][c - 1]
            octopus.val += 1
        # Up-Left
        if c > 0 and r > 0:
            octopus = self.octopus_grid[r - 1][c - 1]
            octopus.val += 1
        # Up
        if r > 0:
            octopus = self.octopus_grid[r - 1][c]
            octopus.val += 1
        # Up-Right
        if r > 0 and c < 9:
            octopus = self.octopus_grid[r - 1][c + 1]
            octopus.val += 1
        # Right
        if c < 9:
            octopus = self.octopus_grid[r][c + 1]
            octopus.val += 1
        # Down-Right
        if r < 9 and c < 9:
            octopus = self.octopus_grid[r + 1][c + 1]
            octopus.val += 1
        # Down
        if r < 9:
            octopus = self.octopus_grid[r + 1][c]
            octopus.val += 1
        # Down-Left
        if r < 9 and c > 0:
            octopus = self.octopus_grid[r + 1][c - 1]
            octopus.val += 1

    def clear_octopus(self) -> None:
        for octopus_row in self.octopus_grid:
            for octopus in octopus_row:
                octopus.clear()
        if len(self.flashed.keys()) == 100:
            self.sync_step = self.step
        self.flashed = {}


def _parse_input(filename: str) -> List[List[DumboOctopus]]:
    octopus_grid = []
    with open(filename) as f:
        for line in f.readlines():
            octopus_grid.append([DumboOctopus(int(x)) for x in line.strip()])
    return octopus_grid


if __name__ == "__main__":
    # Parse input
    example_octopus_state = DumboOctopusState(
        octopus_grid=_parse_input("11-input-example.txt")
    )
    octopus_state = DumboOctopusState(octopus_grid=_parse_input("11-input.txt"))

    # Part 1
    example_octopus_state.run_n_steps(steps=100)
    assert example_octopus_state.total_flashes == 1656

    octopus_state.run_n_steps(steps=100)
    print(octopus_state.total_flashes)

    # Part 2
    example_octopus_state.run_until_sync()
    assert example_octopus_state.step == 195

    octopus_state.run_until_sync()
    print(octopus_state.step)
