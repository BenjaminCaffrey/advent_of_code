def calc_position():
    x = 0
    y = 0
    with open("2-input.txt") as f:
        commands = f.readlines()

    for command in commands:
        command_direction, command_units = command.split(" ")
        if command_direction == "forward":
            x += int(command_units)
        elif command_direction == "down":
            y += int(command_units)
        elif command_direction == "up":
            y -= int(command_units)
        else:
            raise ("Unsupported command!")

    return x * y


def calc_position_with_aim():
    x = 0
    y = 0
    cur_aim = 0

    with open("2-input.txt") as f:
        commands = f.readlines()

    for command in commands:
        command_direction, command_units = command.split(" ")
        if command_direction == "forward":
            x += int(command_units)
            y += int(command_units) * cur_aim
        elif command_direction == "down":
            cur_aim += int(command_units)
        elif command_direction == "up":
            cur_aim -= int(command_units)
        else:
            raise ("Unsupported command!")

    return x * y


if __name__ == "__main__":
    result = calc_position()
    print(result)

    result = calc_position_with_aim()
    print(result)
