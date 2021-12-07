from typing import List, Dict


def memo_days() -> Dict[int, int]:
    cur_fish = [0]
    num_fish_on_day = {}

    for i in range(1, 80):
        next_fish = []
        for fish in cur_fish:
            if fish > 0:
                next_fish.append(fish - 1)
            elif fish == 0:
                next_fish.extend([6, 8])
        num_fish_on_day[i] = len(next_fish)
        cur_fish = next_fish

    return num_fish_on_day


def calc_total_fish(
    fish_list: List[int], day: int, num_fish_on_day: Dict[int, int]
) -> int:
    sum_fish = 0
    for fish in fish_list:
        sum_fish += num_fish_on_day[day - fish]
    return sum_fish


def _parse_input(filename: str) -> List[int]:
    with open(filename) as f:
        fish = [int(x.strip()) for x in f.readline().split(",")]
    return fish


if __name__ == "__main__":
    num_fish_on_day = memo_days()

    fish_list = _parse_input("6-input-example.txt")
    sum_fish = calc_total_fish(fish_list, 80, num_fish_on_day)
    assert sum_fish == 5934

    fish_list = _parse_input("6-input.txt")
    sum_fish = calc_total_fish(fish_list, 80, num_fish_on_day)
    print(sum_fish)

    fish_list = _parse_input("6-input.txt")
    sum_fish = calc_total_fish(fish_list, 80, num_fish_on_day)
    print(sum_fish)
