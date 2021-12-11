# aoc_day_11.py

from collections import defaultdict
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return_list = list()
        for line in puzzle_input.split("\n"):
            line_list = list()
            for number in list(line):
                line_list.append(int(number))
            return_list.append(line_list)
        return return_list

    @classmethod
    def get_day(cls):
        return 11

    @staticmethod
    def flash(x, y, octo):
        octo[(x + 1, y)][0] += 1
        octo[(x + 1, y + 1)][0] += 1
        octo[(x, y + 1)][0] += 1
        octo[(x, y - 1)][0] += 1
        octo[(x - 1, y)][0] += 1
        octo[(x - 1, y - 1)][0] += 1
        octo[(x - 1, y + 1)][0] += 1
        octo[(x + 1, y - 1)][0] += 1

    def simulate_flashes(self, max_iterations=False):
        octo = defaultdict(lambda: [0, False])
        iteration = 0
        total_flash_count = 0

        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                octo[(x, y)] = [int(col), False]

        while not max_iterations or iteration < max_iterations:
            local_flash_count = 0

            for y in range(len(self.data)):
                for x in range(len(self.data[0])):
                    octo[(x, y)][0] += 1

            flashing = True
            while flashing:
                flashing = False
                for y in range(len(self.data)):
                    for x in range(len(self.data[0])):
                        if octo[(x, y)][0] > 9 and not octo[(x, y)][1]:
                            flashing = True
                            octo[(x, y)][1] = True
                            self.flash(x, y, octo)
                            local_flash_count += 1
                            total_flash_count += 1
            iteration += 1
            if local_flash_count == len(self.data) * len(self.data[0]):
                break

            for y in range(len(self.data)):
                for x in range(len(self.data[0])):
                    if octo[(x, y)][1]:
                        octo[(x, y)][0] = 0
                        octo[(x, y)][1] = False

        return total_flash_count, iteration

    def part1(self):
        """Solve part 1"""
        return self.simulate_flashes(100)[0]

    def part2(self):
        """Solve part 2"""
        return self.simulate_flashes()[1]


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
