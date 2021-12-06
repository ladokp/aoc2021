# aoc_day_04.py

import copy
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, file_name):
        self.drawn_numbers = list()
        self.boards_list = list()
        super().__init__(file_name)

    def _parse(self, puzzle_input):
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

    def _find_winning_boards(self):
        boards_list = copy.deepcopy(self.boards_list)
        first_board_score = 0
        last_board_score = 0
        for drawn_number in self.drawn_numbers:
            finished_boards = list()
            for index_, board in enumerate(boards_list):
                boards_list[index_] = self.mark_number(board, drawn_number)
                if self.is_complete_rows_cols(board):
                    if not first_board_score:
                        first_board_score = self.calculate_score(
                            boards_list[index_], drawn_number
                        )
                    finished_boards.insert(0, index_)
                    continue

            for index_ in finished_boards:
                if len(boards_list) == 1:
                    last_board_score = self.calculate_score(
                        boards_list[index_], drawn_number
                    )
                boards_list.pop(index_)
        return first_board_score, last_board_score

    def part1(self):
        """Solve part 1"""
        return self._find_winning_boards()[0]

    def part2(self):
        """Solve part 2"""
        return self._find_winning_boards()[1]


if __name__ == "__main__":
    exercise_solution = AocSolution("day_04.txt")
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
