# aoc_day_02.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return_list = list()
        for line in puzzle_input.split("\n"):
            split_line = line.split(" ")
            return_list.append((split_line[0], int(split_line[1])))

        return return_list

    def _calculate_metrics(self):
        horizontal_position = 0
        depth1 = 0
        depth2 = 0
        aim = 0

        for command, unit in self.data:
            if command == "forward":
                horizontal_position += unit
                depth2 += aim * unit
            elif command == "down":
                aim += unit
                depth1 += unit
            elif command == "up":
                aim -= unit
                depth1 -= unit

        return horizontal_position * depth1, horizontal_position * depth2

    def part1(self):
        """Solve part 1"""
        return self._calculate_metrics()[0]

    def part2(self):
        """Solve part 2"""
        return self._calculate_metrics()[1]


if __name__ == "__main__":
    exercise_solution = AocSolution("day_02.txt")
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
