# aoc_day_15.py

import heapq
import math
import numpy as np
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    @classmethod
    def get_day(cls):
        return 15

    def _parse(self, puzzle_input):
        """Parse input"""
        return np.array(
            [[int(x) for x in line.rstrip()] for line in puzzle_input.split("\n")]
        )

    def neighbors(self, x, y):
        if x > 0:
            yield x - 1, y
        if x < self.data.shape[0] - 1:
            yield x + 1, y
        if y > 0:
            yield x, y - 1
        if y < self.data.shape[1] - 1:
            yield x, y + 1

    def find_path(self):
        border = [(0, (0, 0))]
        length_so_far = {(0, 0): 0}
        while border:
            length, (x, y) = heapq.heappop(border)
            if (x + 1, y + 1) == self.data.shape:
                return length
            for neighbor in self.neighbors(x, y):
                new_length = length + self.data[neighbor]
                if new_length < length_so_far.get(neighbor, math.inf):
                    heapq.heappush(border, (new_length, neighbor))
                    length_so_far[neighbor] = new_length

    def part1(self):
        """Solve part 1"""
        return self.find_path()

    def part2(self):
        """Solve part 2"""
        self.data = np.concatenate(
            [((self.data + i - 1) % 9) + 1 for i in range(5)], axis=0
        )
        self.data = np.concatenate(
            [((self.data + i - 1) % 9) + 1 for i in range(5)], axis=1
        )

        return self.find_path()


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
