# aoc_day_05.py

from collections import defaultdict
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.hor_vert_lines_dict = defaultdict(lambda: 0)
        self.all_lines_dict = defaultdict(lambda: 0)
        super().__init__(test_suffix=test_suffix)

    @classmethod
    def get_day(cls):
        return 5

    def _parse(self, puzzle_input):
        """Parse input"""
        for line in puzzle_input.split("\n"):
            tmp_list = list()
            for point in line.split(" -> "):
                x, y = point.split(",")
                tmp_list.append((int(x), int(y)))
            self._count_lines(tmp_list)

    def _count_lines(self, coordinate_list):
        if coordinate_list[0][0] == coordinate_list[1][0]:
            coordinate_list.sort(key=lambda z: z[1])
            start, end = [*coordinate_list]
            x = start[0]
            for y in range(start[1], end[1] + 1):
                self.hor_vert_lines_dict[(x, y)] += 1
                self.all_lines_dict[(x, y)] += 1
        elif coordinate_list[0][1] == coordinate_list[1][1]:
            coordinate_list.sort(key=lambda z: z[0])
            start, end = [*coordinate_list]
            y = start[1]
            for x in range(start[0], end[0] + 1):
                self.hor_vert_lines_dict[(x, y)] += 1
                self.all_lines_dict[(x, y)] += 1
        else:
            start, end = [*coordinate_list]
            self._count_diagonal_points(start[0], start[1], end[0], end[1])

    def _count_diagonal_points(self, start_x, start_y, end_x, end_y):
        # make start_x <= end_x
        if start_x > end_x:
            start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

        slope = (end_y - start_y) // (end_x - start_x)
        for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
            self.all_lines_dict[(i, j)] += 1

        self.all_lines_dict[(end_x, end_y)] += 1

    @staticmethod
    def _count_dangerous_points(point_dict):
        overlapping_points = dict(filter(lambda elem: elem[1] >= 2, point_dict.items()))
        return len(overlapping_points)

    def part1(self):
        """Solve part 1"""
        return AocSolution._count_dangerous_points(self.hor_vert_lines_dict)

    def part2(self):
        """Solve part 2"""
        return AocSolution._count_dangerous_points(self.all_lines_dict)


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
