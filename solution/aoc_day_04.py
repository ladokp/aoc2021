# aoc_day_04.py
import copy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.drawn_numbers = list()
        self.boards_list = list()
        self.initial_board_list = None
        self.winning_boards = list()

    def parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.split("\n\n")
        self.drawn_numbers = [int(number) for number in puzzle_input.pop(0).split(",")]
        for board in puzzle_input:
            board = board.split("\n")
            current_board = list()
            for line in board:
                line = [
                    int(number) for number in line.split(" ") if f"{number}".isdigit()
                ]
                current_board.append(line)
            self.boards_list.append(current_board)
        self.initial_board_list = copy.deepcopy(self.boards_list)
        return self.drawn_numbers, self.boards_list

    @staticmethod
    def mark_number(board, drawn_number):
        for y, row in enumerate(board):
            for x, num in enumerate(row):
                if num == drawn_number:
                    board[y][x] = "x"
        return board

    @staticmethod
    def calculate_score(board, drawn_number):
        score = 0
        for y, row in enumerate(board):
            for x, num in enumerate(row):
                if num != "x":
                    score += num
        return score * drawn_number

    @staticmethod
    def is_complete_rows_cols(board):
        for row in board:
            if row.count("x") == len(row):
                return True

        board = [list(i) for i in zip(*board)]
        for col in board:
            if col.count("x") == len(col):
                return True
        return False

    def part1(self, data):
        """Solve part 1"""
        for drawn_number in self.drawn_numbers:
            for index_, board in enumerate(self.boards_list):
                self.boards_list[index_] = self.mark_number(board, drawn_number)
                if self.is_complete_rows_cols(board):
                    return self.calculate_score(board, drawn_number)

    def part2(self, data):
        """Solve part 2"""
        self.boards_list = copy.deepcopy(self.initial_board_list)
        for drawn_number in self.drawn_numbers:
            finished_boards = list()
            for index_, board in enumerate(self.boards_list):
                self.boards_list[index_] = self.mark_number(board, drawn_number)
                if self.is_complete_rows_cols(board):
                    finished_boards.insert(0, index_)
                    continue

            for index_ in finished_boards:
                if len(self.boards_list) == 1:
                    return self.calculate_score(self.boards_list[0], drawn_number)
                if self.boards_list[index_]:
                    self.boards_list.pop(index_)


if __name__ == "__main__":
    AocSolution("day_04.txt").run_aoc_solution()
