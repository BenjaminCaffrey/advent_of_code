def sonar_sweep():
    increasing_depth_count = 0

    with open("1-input.txt") as f:
        depths = f.readlines()
        depths = [int(x) for x in depths]
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increasing_depth_count += 1

    return increasing_depth_count


def sonar_sweep_rolling_average():
    increasing_depth_count = 0
    with open("1-input.txt") as f:
        depths = f.readlines()
        depths = [int(depth) for depth in depths]
        rolling_depths = [sum(depths[x : x + 3]) for x in range(0, len(depths) - 2)]
    for i in range(1, len(rolling_depths)):
        if rolling_depths[i] > rolling_depths[i - 1]:
            increasing_depth_count += 1
    return increasing_depth_count


if __name__ == "__main__":
    result = sonar_sweep()
    print(result)

    result = sonar_sweep_rolling_average()
    print(result)
