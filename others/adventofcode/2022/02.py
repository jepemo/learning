from typing import List
from common import *

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# Score:
# 1 for Rock, 2 for Paper, and 3 for Scissors
# +
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

symbol_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

game_result = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}


def get_score(opponent, you):
    return symbol_score[you] + game_result[opponent + you]


# X lose, Y draw, and Z win
game_symbol = {
    "YA": "X",
    "YB": "Y",
    "YC": "Z",
    "XA": "Z",
    "XB": "X",
    "XC": "Y",
    "ZA": "Y",
    "ZB": "Z",
    "ZC": "X",
}


def get_score_2(opponent, result):
    symbol = game_symbol[result + opponent]
    return symbol_score[symbol] + game_result[opponent + symbol]


def day2_1(games: List[str]) -> int:
    score = 0
    for game in games:
        [opponent, you] = game.split()
        score += get_score(opponent, you)

    return score


def day2_2(games: List[str]) -> int:
    score = 0
    for game in games:
        [opponent, you] = game.split()
        score += get_score_2(opponent, you)

    return score


if __name__ == "__main__":
    data = read_data(2, parser=str, test=True)
    do(2, data, answers=[15, 12], test=True)
    data = read_data(2, parser=str)
    do(2, data, answers=[9759, 12429])
