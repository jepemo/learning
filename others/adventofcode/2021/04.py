from common import *

BOARD_DIM = 5


class Board:
    def __init__(self):
        self.numbers = []
        self.matches = []

    @staticmethod
    def create_from_lines(input_lines):
        board = Board()
        for line in input_lines:
            vals = list(map(int, line.strip().split()))
            board.numbers.append(vals)
            board.matches.append([False for _x in range(BOARD_DIM)])

        return board

    def mark(self, value):
        for i in range(BOARD_DIM):
            for j in range(BOARD_DIM):
                if self.numbers[i][j] == value:
                    self.matches[i][j] = True

    def is_winner(self):
        # Rows
        for i in range(BOARD_DIM):
            if sum(self.matches[i]) == BOARD_DIM:
                return True

        # Cols
        for j in range(BOARD_DIM):
            if sum([self.matches[i][j] for i in range(BOARD_DIM)]) == BOARD_DIM:
                return True

        return False

    def get_not_marked(self):
        nm = []
        for i in range(BOARD_DIM):
            for j in range(BOARD_DIM):
                if not self.matches[i][j]:
                    nm.append(self.numbers[i][j])

        return nm

    def __str__(self):
        return f"{self.matches}"


def read_drawn_numbers(line: str):
    return list(map(int, line.strip().split(',')))


def read_game_data(test=False):
    filename = "data/input4.txt" if not test else "data/test4.txt"
    lines = open(filename).readlines()
    drawn_numbers = read_drawn_numbers(lines[0])
    boards = []

    num_lines = len(lines)
    file_row = 2
    while file_row < num_lines:
        boards.append(Board.create_from_lines(
            lines[file_row:file_row+BOARD_DIM]))
        file_row += BOARD_DIM + 1

    return (drawn_numbers, boards)


def day4_1(data):
    (drawn_numbers, boards) = data
    for num in drawn_numbers:
        for board in boards:
            board.mark(num)
            if board.is_winner():
                nm = board.get_not_marked()
                return sum(nm) * num

    return -1


def day4_2(data):
    winers = []
    (drawn_numbers, boards) = data
    for num in drawn_numbers:
        for p_board, board in enumerate(boards):
            board.mark(num)
            if board.is_winner():
                if not p_board in winers:
                    winers.append(p_board)

                if len(winers) == len(boards):
                    nm = board.get_not_marked()
                    return sum(nm) * num


if __name__ == "__main__":
    data = read_game_data(test=True)
    do(4, data, answers=[4512, 1924], test=True)

    data = read_game_data()
    do(4, data, answers=[49860, 0])
