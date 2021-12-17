# aoc_day_17.py

from solution.aoc_base import AocBaseClass
import re


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        target_area = map(int, re.findall(r"\d+", puzzle_input))
        return tuple(i * j for i, j in zip(target_area, [1, 1, -1, -1]))

    DAY = 17

    def find_target_area(self, /, calculate_score=False):
        x_min, x_max, y_min, y_max = self.data
        y_v_max, score = int(y_min * (y_min + 1) / 2), 0

        if calculate_score:
            for i in range(y_min - 1, -y_min + 1):
                for j in range(x_max + 1):
                    x, y, ci, cj = 0, 0, i, j
                    while x < x_max and y > y_min:
                        x += cj
                        y += ci
                        if x in range(x_min, x_max + 1) and y in range(
                            y_min, y_max + 1
                        ):
                            score += 1
                            break

                        ci -= 1
                        if cj > 0:
                            cj -= 1
        return y_v_max, score

    def part1(self):
        """Solve part 1"""
        return self.find_target_area()

    def part2(self):
        """Solve part 2"""
        return self.find_target_area(calculate_score=True)


if __name__ == "__main__":
    AocSolution().print_solution()
