'''
First column: A -> Rock, B -> Paper, C -> Scissors
Second column: X -> Rock, Y -> Paper, Z -> Scissors

The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the 
outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
'''
class Part1:
    GAME_SCORE_GUIDE = {
        "A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3},
    }

    SYMBOL_SCORE_GUIDE = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    def calculate_rps_score(self):
        total_score = 0
        with open("2-input.txt") as f:
            for line in f.readlines():
                total_score += self.calculate_round_score(line.strip())
        return total_score

    def calculate_round_score(self, encoded_game):
        opp_symbol, self_symbol = encoded_game.split(" ")

        game_score = self.GAME_SCORE_GUIDE[opp_symbol][self_symbol]
        symbol_score = self.SYMBOL_SCORE_GUIDE[self_symbol]
        
        return game_score + symbol_score

'''
The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the 
outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
'''
class Part2:
    SYMBOL_SCORE_GUIDE = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1},
    }

    GAME_SCORE_GUIDE = {
        "X": 0,
        "Y": 3,
        "Z": 6,
    }

    def calculate_rps_score(self):
        total_score = 0
        with open("2-input.txt") as f:
            for line in f.readlines():
                total_score += self.calculate_round_score(line.strip())
        return total_score

    def calculate_round_score(self, encoded_game):
        opp_symbol, outcome_symbol = encoded_game.split(" ")

        game_score = self.GAME_SCORE_GUIDE[outcome_symbol]
        symbol_score = self.SYMBOL_SCORE_GUIDE[opp_symbol][outcome_symbol]
        
        return game_score + symbol_score


if __name__ == "__main__":
    pt1 = Part1()
    result = pt1.calculate_rps_score()
    print(result)

    pt2 = Part2()
    result = pt2.calculate_rps_score()
    print(result)