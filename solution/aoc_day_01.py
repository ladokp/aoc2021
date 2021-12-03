# aoc_day_01.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def parse(self, puzzle_input):
        """Parse input"""
        return [int(line) for line in puzzle_input.split("\n")]

    def part1(self, data, group_size=1):
        """Solve part 1"""
        increasing_measurements = 0

        for index, _ in enumerate(data):
            if index <= group_size - 1:
                continue
            if sum(data[index - (group_size - 1) : index + 1]) > sum(
                data[index - group_size : index]
            ):
                increasing_measurements += 1

        return increasing_measurements

    def part2(self, data, group_size=3):
        """Solve part 2"""
        return self.part1(data, group_size)


if __name__ == "__main__":
    AocSolution("day_01.txt").run_aoc_solution()
