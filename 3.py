from collections import defaultdict


def calc_power_consumption(filename: str) -> int:
    binary_inputs = _parse_input(filename)
    digit_counts = _get_all_digit_counts(binary_inputs)

    gamma_rate_digits = []
    epsilon_rate_digits = []

    for digit in digit_counts:
        if digit > len(binary_inputs) / 2:
            gamma_rate_digits.append("1")
            epsilon_rate_digits.append("0")
        else:
            gamma_rate_digits.append("0")
            epsilon_rate_digits.append("1")

    gamma_rate = _binary_char_list_to_decimal(gamma_rate_digits)
    epsilon_rate = _binary_char_list_to_decimal(epsilon_rate_digits)

    return gamma_rate * epsilon_rate


def calc_life_support_rating(filename: str) -> int:
    binary_inputs = _parse_input(filename)

    starts_with_dict = defaultdict(list)
    for binary_input in binary_inputs:
        for i in range(1, len(binary_input) + 1):
            starts_with_dict[binary_input[0:i]].append(binary_input)

    cur_binary_inputs = binary_inputs
    oxygen_generator_rating_start = ""
    n = 0
    while True:
        cur_digit_count = _get_nth_digit_count(cur_binary_inputs, n)
        if cur_digit_count >= len(cur_binary_inputs) / 2:
            oxygen_generator_rating_start += "1"
        else:
            oxygen_generator_rating_start += "0"

        cur_binary_inputs = starts_with_dict[oxygen_generator_rating_start]
        n += 1
        if len(cur_binary_inputs) == 1:
            oxygen_generator_rating = list(cur_binary_inputs[0])
            break

    cur_binary_inputs = binary_inputs
    co2_scrubber_rating_start = ""
    n = 0
    while True:
        cur_digit_count = _get_nth_digit_count(cur_binary_inputs, n)
        if cur_digit_count >= len(cur_binary_inputs) / 2:
            co2_scrubber_rating_start += "0"
        else:
            co2_scrubber_rating_start += "1"

        cur_binary_inputs = starts_with_dict[co2_scrubber_rating_start]
        n += 1
        if len(cur_binary_inputs) == 1:
            co2_scrubber_rating = list(cur_binary_inputs[0])
            break

    oxygen_generator_rating = _binary_char_list_to_decimal(oxygen_generator_rating)
    co2_scrubber_rating = _binary_char_list_to_decimal(co2_scrubber_rating)
    return oxygen_generator_rating * co2_scrubber_rating


## Helpers
def _parse_input(filename: str):
    with open(filename) as f:
        binary_inputs = f.readlines()
        binary_inputs = [x.strip() for x in binary_inputs]
        return binary_inputs


def _get_all_digit_counts(binary_inputs):
    digit_counts = [0] * len(binary_inputs[0])
    for binary_input in binary_inputs:
        for i, char in enumerate(binary_input):
            if int(char) == 1:
                digit_counts[i] += 1
    return digit_counts


def _get_nth_digit_count(binary_inputs, n):
    digit_count = 0
    for binary_input in binary_inputs:
        if binary_input[n] == "1":
            digit_count += 1
    return digit_count


def _binary_char_list_to_decimal(binary_str_list: str):
    return int("".join(binary_str_list), 2)


## Main
if __name__ == "__main__":
    assert calc_power_consumption("3-input-example.txt") == 198
    result = calc_power_consumption("3-input.txt")
    print(result)

    assert calc_life_support_rating("3-input-example.txt") == 230
    result = calc_life_support_rating("3-input.txt")
    print(result)
