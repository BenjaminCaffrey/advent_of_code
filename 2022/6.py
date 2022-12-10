def is_unique(chars: str):
    char_dict = {}
    for char in chars:
        if char in char_dict:
            return False
        else:
            char_dict[char] = True
    return True

def find_distinct_char_marker(n: int):
    with open("6-input.txt") as f:
        signal = f.readline().strip()

        for i in range(n, len(signal)):
            if is_unique(signal[i-n:i]):
                return i



if __name__ == "__main__":
    result = find_distinct_char_marker(4)
    print(result)

    result = find_distinct_char_marker(14)
    print(result)