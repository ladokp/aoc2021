# aoc_day_10.py

from solution.aoc_base import AocBaseClass


class CorruptException(Exception):
    def __init__(self, error_code):
        super().__init__("line is corrupt")
        self.error_code = error_code


class IncompleteException(Exception):
    def __init__(self, error_code):
        super().__init__("line is incomplete")
        self.error_code = error_code


class AocSolution(AocBaseClass):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.bracket = {"{": "}", "(": ")", "[": "]", "<": ">"}
        self.corrupt_brackets = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self.incomplete_brackets = {"(": 1, "[": 2, "{": 3, "<": 4}

    def _parse(self, puzzle_input):
        """Parse input"""
        return [line for line in puzzle_input.split("\n")]

    def check_chunks(self):
        def check_sub_chunk(pos):
            while True:
                if pos >= len(line):
                    raise IncompleteException(0)

                start = line[pos]
                if start not in self.bracket.keys():
                    return pos

                try:
                    pos = check_sub_chunk(pos + 1)
                except IncompleteException as e:
                    raise IncompleteException(e.error_code * 5 + self.incomplete_brackets[start])

                end = line[pos]
                if end != self.bracket[start]:
                    raise CorruptException(self.corrupt_brackets[end])
                pos += 1

        corrupt_counter = 0
        incomplete_list = list()
        for line in self.data:
            try:
                check_sub_chunk(0)
            except CorruptException as corrupt:
                corrupt_counter += corrupt.error_code
            except IncompleteException as incomplete:
                incomplete_list.append(incomplete.error_code)

        return corrupt_counter, incomplete_list

    def part1(self):
        """Solve part 1"""
        return self.check_chunks()[0]

    def part2(self):
        """Solve part 2"""
        scores = self.check_chunks()[1]
        return sorted(scores)[len(scores) >> 1]


if __name__ == "__main__":
    exercise_solution = AocSolution("day_10.txt")
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
