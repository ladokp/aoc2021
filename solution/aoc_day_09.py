# aoc_day_09.py

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
        return 9

    def is_low_point(self, x, y):
        underground_map_matrix = self.data
        current_point = underground_map_matrix[y][x]
        x_max_index = len(underground_map_matrix[y]) - 1
        y_max_index = len(underground_map_matrix) - 1

        if x > 0 and underground_map_matrix[y][x - 1] <= current_point:  # left
            return False
        if (
            x < x_max_index and underground_map_matrix[y][x + 1] <= current_point
        ):  # right
            return False
        if y > 0 and underground_map_matrix[y - 1][x] <= current_point:  # up
            return False
        if (
            y < y_max_index and underground_map_matrix[y + 1][x] <= current_point
        ):  # down
            return False
        return True

    def flood_recursive(self, start_x, start_y, new_number):
        matrix = self.data
        width = len(matrix[0])
        height = len(matrix)

        def fill(x, y, fill_number, boundary_number=9):
            if matrix[y][x] in [fill_number, boundary_number] or matrix[y][x] < 0:
                return
            else:
                matrix[y][x] = fill_number
                neighbors = [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ]
                for n in neighbors:
                    if 0 <= n[0] <= width - 1 and 0 <= n[1] <= height - 1:
                        fill(n[0], n[1], fill_number, boundary_number)

        return fill(start_x, start_y, new_number)

    def part1(self):
        """Solve part 1"""
        low_points_risk = 0
        low_points_list = list()
        for y, row in enumerate(self.data):
            for x, col in enumerate(row):
                if self.is_low_point(x, y):
                    low_points_list.append((x, y))
                    low_points_risk += col + 1
        return low_points_risk, low_points_list

    def part2(self):
        """Solve part 2"""
        _, low_points_coordinates = self.part1()
        basin_colors = range(-1, (len(low_points_coordinates) + 1) * -1, -1)
        for low_points, new_number in zip(low_points_coordinates, basin_colors):
            self.flood_recursive(*low_points, new_number)

        basin_areas = defaultdict(lambda: 0)
        for line in self.data:
            for color in basin_colors:
                basin_areas[color] += line.count(color)
        basin_areas = list(basin_areas.values())
        basin_areas.sort(reverse=True)

        return basin_areas[0] * basin_areas[1] * basin_areas[2]


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
