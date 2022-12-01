from typing import DefaultDict, List, Dict


def memo_days() -> Dict[int, int]:
    num_fish_on_day = {0: 1}
    num_zeros_on_day = DefaultDict(int)
    num_zeros_on_day[0] = 1

    for i in range(0, 256):
        if num_zeros_on_day[i]:
            num_zeros_on_day[i + 7] += num_zeros_on_day[i]
            num_zeros_on_day[i + 9] += num_zeros_on_day[i]
        num_fish_on_day[i + 1] = num_fish_on_day[i] + num_zeros_on_day[i]
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
    print(num_fish_on_day)

    fish_list = _parse_input("6-input-example.txt")
    sum_fish = calc_total_fish(fish_list, 80, num_fish_on_day)
    assert sum_fish == 5934

    fish_list = _parse_input("6-input.txt")
    sum_fish = calc_total_fish(fish_list, 80, num_fish_on_day)
    print(sum_fish)

    fish_list = _parse_input("6-input.txt")
    sum_fish = calc_total_fish(fish_list, 256, num_fish_on_day)
    print(sum_fish)
