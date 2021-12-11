from typing import List
from dataclasses import dataclass

OPEN_CHARS = ["(", "[", "{", "<"]
CLOSE_CHARS = [")", "]", "}", ">"]
OPEN_CHAR_PAIRING = {"(": ")", "[": "]", "{": "}", "<": ">"}
CLOSE_CHAR_PAIRING = {")": "(", "]": "[", "}": "{", ">": "<"}
CLOSE_CHAR_ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSE_CHAR_AUTOCOMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


@dataclass
class LineOutput:
    error_score: int = 0
    autocomplete_score: int = 0


def calc_syntax_error_score(lines: List[str]) -> int:
    syntax_error_score = 0
    for line in lines:
        syntax_error_score += parse_line(line).error_score
    return syntax_error_score


def calc_autocomplete_score(lines: List[str]) -> int:
    autocomplete_scores = []
    for line in lines:
        autocomplete_score = parse_line(line).autocomplete_score
        if autocomplete_score:
            autocomplete_scores.append(autocomplete_score)
    return sorted(autocomplete_scores)[len(autocomplete_scores) // 2]


def parse_line(line: str) -> LineOutput:
    line_output = LineOutput()
    stack = []
    for char in line:
        if char in OPEN_CHARS:
            stack.append(char)
        elif char in CLOSE_CHARS:
            if stack[-1] == CLOSE_CHAR_PAIRING[char]:
                stack.pop()
            else:
                line_output.error_score = CLOSE_CHAR_ERROR_SCORE[char]
                return line_output

    closing_chars = [OPEN_CHAR_PAIRING[x] for x in stack][::-1]
    for char in closing_chars:
        line_output.autocomplete_score *= 5
        line_output.autocomplete_score += CLOSE_CHAR_AUTOCOMPLETE_SCORE[char]
    return line_output


def _parse_input(filename: str) -> List[str]:
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    # Parse inputs
    example_lines = _parse_input("10-input-example.txt")
    lines = _parse_input("10-input.txt")

    # Part 1
    syntax_error_score = calc_syntax_error_score(example_lines)
    assert syntax_error_score == 26397

    syntax_error_score = calc_syntax_error_score(lines)
    print(syntax_error_score)

    # Part 2
    autocomplete_score = calc_autocomplete_score(example_lines)
    assert autocomplete_score == 288957

    autocomplete_score = calc_autocomplete_score(lines)
    print(autocomplete_score)
