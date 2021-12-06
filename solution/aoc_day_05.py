# aoc_day_05.py

from collections import defaultdict
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return_list = list()
        for line in puzzle_input.split("\n"):
            tmp_list = list()
            for point in line.split(" -> "):
                x, y = point.split(",")
                tmp_list.append((int(x), int(y)))
            return_list.append(self._fill_line(tmp_list))
        return return_list

    @staticmethod
    def _fill_line(coordinate_list):
        if coordinate_list[0][0] == coordinate_list[1][0]:
            coordinate_list.sort(key=lambda z: z[1])
            start, end = [*coordinate_list]
            filled_line = [start, end]
            x = start[0]
            for y in range(start[1] + 1, end[1]):
                filled_line.append((x, y))
        elif coordinate_list[0][1] == coordinate_list[1][1]:
            coordinate_list.sort(key=lambda z: z[0])
            start, end = [*coordinate_list]
            filled_line = [start, end]
            y = start[1]
            for x in range(start[0] + 1, end[0]):
                filled_line.append((x, y))
        else:
            start, end = [*coordinate_list]
            filled_line = AocSolution._get_diagonal_points(
                start[0], start[1], end[0], end[1]
            )

        return filled_line

    @staticmethod
    def _get_diagonal_points(start_x, start_y, end_x, end_y):
        # make start_x <= end_x
        if start_x > end_x:
            start_x, start_y, end_x, end_y = end_x, end_y, start_x, start_y

        result = []
        slope = (end_y - start_y) // (end_x - start_x)
        for i, j in zip(range(start_x, end_x), range(start_y, end_y, slope)):
            result.append((i, j))
        result.append((end_x, end_y))  # add end point
        return result

    def _find_overlapping_points(self, /, count_diagonals=False):
        lines_to_count = self.data
        if not count_diagonals:
            lines_to_count = [
                element
                for element in self.data
                if element[0][0] == element[1][0] or element[0][1] == element[1][1]
            ]
        count_points_dict = defaultdict(lambda: 0)
        for line in lines_to_count:
            for point in line:
                count_points_dict[point] += 1
        overlapping_points = dict(
            filter(lambda elem: elem[1] >= 2, count_points_dict.items())
        )
        return len(overlapping_points)

    def part1(self):
        """Solve part 1"""
        return self._find_overlapping_points()

    def part2(self):
        """Solve part 2"""
        return self._find_overlapping_points(count_diagonals=True)


if __name__ == "__main__":
    exercise_solution = AocSolution("day_05.txt")
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
