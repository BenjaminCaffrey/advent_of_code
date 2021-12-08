from typing import List, Dict

DISPLAY_MAP = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


class SubmarineNote:
    def __init__(self, signal_patterns: List[str], output_values: List[str]) -> None:
        self.signal_patterns = signal_patterns
        self.output_values = output_values
        self.determine_mapping()

    def map_all_output(self) -> int:
        output_digits = []
        for output in self.output_values:
            new_output = self.map_single_output(output)
            output_digits.append(str(DISPLAY_MAP[new_output]))
        return int("".join(output_digits))

    def map_single_output(self, output: str) -> str:
        new_output = []
        for char in output:
            new_output.append(self.unique_mapping[char])
        return "".join(sorted(new_output))

    def determine_mapping(self) -> None:
        self.unique_mapping: Dict[str, str] = {}
        self.char_counts: Dict[str, int] = {}
        self.map_bef()
        self.map_ac()
        self.map_d()
        self.map_g()

    def map_bef(self) -> None:
        for signal_pattern in self.signal_patterns:
            for char in signal_pattern:
                self.char_counts[char] = self.char_counts.get(char, 0) + 1
        for key, value in self.char_counts.items():
            if value == 4:
                self.unique_mapping[key] = "e"
            elif value == 6:
                self.unique_mapping[key] = "b"
            elif value == 9:
                self.unique_mapping[key] = "f"

    def map_ac(self) -> None:
        signal_1 = [x for x in self.signal_patterns if len(x) == 2][0]
        signal_7 = [x for x in self.signal_patterns if len(x) == 3][0]
        char = next(iter(set(signal_7) - set(signal_1)))
        self.unique_mapping[char] = "a"
        for char in signal_1:
            if char not in self.unique_mapping.keys():
                self.unique_mapping[char] = "c"

    def map_d(self) -> None:
        for signal_pattern in self.signal_patterns:
            if len(signal_pattern) == 4:
                for char in signal_pattern:
                    if char not in self.unique_mapping.keys():
                        self.unique_mapping[char] = "d"

    def map_g(self) -> None:
        char = next(iter(set(list("abcdefg")) - set(self.unique_mapping.keys())))
        self.unique_mapping[char] = "g"


def count_easy_digits(notes: List[SubmarineNote]) -> int:
    num_easy_digits = 0
    for note in notes:
        for value in note.output_values:
            if len(value) in (2, 4, 3, 7):
                num_easy_digits += 1
    return num_easy_digits


def _parse_input(filename: str) -> List[SubmarineNote]:
    notes = []
    with open(filename) as f:
        for line in f.readlines():
            pt1, pt2 = line.split(" | ")
            signal_patterns = [x.strip() for x in pt1.split(" ")]
            output_values = [x.strip() for x in pt2.split(" ")]
            notes.append(SubmarineNote(signal_patterns, output_values))
    return notes


if __name__ == "__main__":
    notes = _parse_input("8-input-example.txt")
    assert count_easy_digits(notes) == 26

    notes = _parse_input("8-input.txt")
    print(count_easy_digits(notes))

    notes = _parse_input("8-input-example.txt")
    sum = 0
    for note in notes:
        sum += note.map_all_output()
    assert sum == 61229

    notes = _parse_input("8-input.txt")
    sum = 0
    for note in notes:
        sum += note.map_all_output()
    print(sum)
