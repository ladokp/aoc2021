# aoc_day_06.py
import copy

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, file_name):
        self.initial_data = None
        super().__init__(file_name)

    def _parse(self, puzzle_input):
        """Parse input"""
        self.initial_data = [int(number) for number in puzzle_input.split(",")]
        return self.initial_data

    def _simulate_population(self, days=80):
        self.data = copy.deepcopy(self.initial_data)
        population = {
            0: self.data.count(0),
            1: self.data.count(1),
            2: self.data.count(2),
            3: self.data.count(3),
            4: self.data.count(4),
            5: self.data.count(5),
            6: self.data.count(6),
            7: self.data.count(7),
            8: self.data.count(8),
        }
        for day_counter in range(0, days):
            population = {
                0: population[1],
                1: population[2],
                2: population[3],
                3: population[4],
                4: population[5],
                5: population[6],
                6: population[7] + population[0],
                7: population[8],
                8: population[0],
            }
        return sum(list(population.values()))

    def part1(self):
        """Solve part 1"""
        return self._simulate_population()

    def part2(self):
        """Solve part 2"""
        return self._simulate_population(256)


if __name__ == "__main__":
    exercise_solution = AocSolution("day_06.txt")
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
