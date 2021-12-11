# aoc_day_01.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return [int(line) for line in puzzle_input.split("\n")]

    @classmethod
    def get_day(cls):
        return 1

    def part1(self, group_size=1):
        """Solve part 1"""
        increasing_measurements = 0

        for index, _ in enumerate(self.data):
            if index <= group_size - 1:
                continue
            if sum(self.data[index - (group_size - 1) : index + 1]) > sum(
                self.data[index - group_size : index]
            ):
                increasing_measurements += 1

        return increasing_measurements

    def part2(self, group_size=3):
        """Solve part 2"""
        return self.part1(group_size)


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
