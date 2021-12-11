# aoc_day_07.py

from collections import defaultdict
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return_list = [int(number) for number in puzzle_input.split(",")]
        return_list.sort()
        return return_list

    @classmethod
    def get_day(cls):
        return 7

    def calculate_cheapest_depth(self):
        def add_consumption(distance):
            depth_fuel_consumption_1[depth].append(distance)
            depth_fuel_consumption_2[depth].append(int((distance * (distance + 1)) / 2))

        depth_fuel_consumption_1 = defaultdict(list)
        depth_fuel_consumption_2 = defaultdict(list)
        for depth in range(1, max(self.data) + 1):
            for diff in self.data:
                add_consumption(abs(diff - depth))
            depth_fuel_consumption_1[depth] = sum(depth_fuel_consumption_1[depth])
            depth_fuel_consumption_2[depth] = sum(depth_fuel_consumption_2[depth])
        return {
            "part1": min(depth_fuel_consumption_1.values()),
            "part2": min(depth_fuel_consumption_2.values()),
        }

    def part1(self):
        """Solve part 1"""
        return self.calculate_cheapest_depth()["part1"]

    def part2(self):
        """Solve part 2"""
        return self.calculate_cheapest_depth()["part2"]


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
