from typing import List
from statistics import median


def calc_fuel_required_1(positions: List[int]) -> int:
    fuel_sum = 0
    target_position = median(positions)
    for position in positions:
        fuel_sum += int(abs(target_position - position))
    return fuel_sum


def calc_fuel_required_2(positions: List[int]) -> int:
    fuel_for_position = []
    for i in range(0, max(positions) + 1):
        fuel_to_i = 0
        for position in positions:
            distance_to_i = abs(i - position)
            fuel_to_i += ((distance_to_i) * (distance_to_i + 1)) // 2
        fuel_for_position.append(fuel_to_i)
    return min(fuel_for_position)


def _parse_input(filename: str) -> List[int]:
    return [int(x.strip()) for x in open(filename).readline().split(",")]


if __name__ == "__main__":
    positions = _parse_input("7-input-example.txt")
    assert calc_fuel_required_1(positions) == 37

    positions = _parse_input("7-input.txt")
    print(calc_fuel_required_1(positions))

    positions = _parse_input("7-input-example.txt")
    assert calc_fuel_required_2(positions) == 168

    positions = _parse_input("7-input.txt")
    print(calc_fuel_required_2(positions))
