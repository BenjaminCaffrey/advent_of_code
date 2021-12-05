from typing import List, Dict


class Bingo:
    def __init__(self, numbers: List[int], boards: List[List[int]]) -> None:
        self.numbers: List[int] = numbers
        self.boards: List[List[int]] = boards
        self.called_numbers: Dict[int, bool] = {}

    def reset(self) -> None:
        self.called_numbers = {}

    def find_winning_board_score(self) -> int:
        for number in self.numbers:
            self.called_numbers[number] = True
            winner = self.check_boards(number)
            if winner:
                return self.calc_board_score(winner, number)

    def find_losing_board_score(self) -> int:
        winning_boards: Dict[int, bool] = {}
        for number in self.numbers:
            self.called_numbers[number] = True
            loser = self.check_boards(
                number, return_last=True, winning_boards=winning_boards
            )
            if loser:
                return self.calc_board_score(loser, number)

    def calc_board_score(self, board: List[List[int]], number: int) -> int:
        uncalled_sum = 0
        for row in board:
            for val in row:
                if val not in self.called_numbers:
                    uncalled_sum += val
        return uncalled_sum * number

    def check_boards(
        self, number: int, return_last=False, winning_boards: Dict[int, bool] = {}
    ) -> List[List[int]]:
        for i, board in enumerate(self.boards):
            for r, row in enumerate(board):
                for c, val in enumerate(row):
                    if val == number:
                        row_wins = self.check_row(board, r)
                        col_wins = self.check_col(board, c)
                        if row_wins or col_wins:
                            if return_last:
                                winning_boards[i] = True
                                if len(winning_boards) == len(self.boards):
                                    return board
                            else:
                                return board

    def check_row(self, board: List[List[int]], row: int) -> bool:
        for val in board[row]:
            if not val in self.called_numbers:
                return False
        return True

    def check_col(self, board: List[List[int]], col: int) -> bool:
        for row in board:
            if not row[col] in self.called_numbers:
                return False
        return True


def _parse_input(filename: str) -> Bingo:
    with open(filename) as f:
        numbers = [int(x) for x in f.readline().split(",")]
        boards: List[List[int]] = []
        cur_board: List[int] = []

        cur_line = f.readline()
        while cur_line:
            cur_line = cur_line.strip()
            if cur_line:
                cur_row: int = [int(x) for x in cur_line.split()]
                if cur_row:
                    cur_board.append(cur_row)
                if len(cur_board) == 5:
                    boards.append(cur_board)
                    cur_board = []
            cur_line = f.readline()

    return Bingo(numbers, boards)


## Main
if __name__ == "__main__":
    # Parse inputs:
    example_game = _parse_input("4-input-example.txt")
    full_game = _parse_input("4-input.txt")

    # Part 1
    winning_board_score = example_game.find_winning_board_score()
    example_game.reset()
    assert winning_board_score == 4512

    winning_board_score = full_game.find_winning_board_score()
    full_game.reset()
    print(winning_board_score)

    # Part 2
    losing_board_score = example_game.find_losing_board_score()
    assert losing_board_score == 1924

    losing_board_score = full_game.find_losing_board_score()
    print(losing_board_score)
