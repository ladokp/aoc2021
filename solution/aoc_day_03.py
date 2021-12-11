# aoc_day_03.py

import copy
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return [list(line) for line in puzzle_input.split("\n")]

    @classmethod
    def get_day(cls):
        return 3

    def part1(self, data=None):
        """Solve part 1"""
        if data is None:
            data = self.data
        transposed_data = [list(i) for i in zip(*data)]
        gamma = list()
        epsilon = list()
        for bit_list in transposed_data:
            ones = bit_list.count("1")
            zeros = bit_list.count("0")
            if ones >= zeros:
                gamma.append("1")
                epsilon.append("0")
            else:
                gamma.append("0")
                epsilon.append("1")

        gamma_ = int("".join(gamma), 2)
        epsilon_ = int("".join(epsilon), 2)
        return gamma_ * epsilon_, "".join(gamma), "".join(epsilon)

    def part2(self):
        """Solve part 2"""
        _, gamma, epsilon = self.part1()

        oxygen_rating = copy.deepcopy(self.data)
        for index, _ in enumerate(gamma):
            bit = self.part1(oxygen_rating)[1][index]
            oxygen_rating = list(filter(lambda x: x[index] == bit, oxygen_rating))
            if len(oxygen_rating) == 1:
                break

        co2_rating = copy.deepcopy(self.data)
        for index, _ in enumerate(epsilon):
            bit = self.part1(co2_rating)[2][index]
            co2_rating = list(filter(lambda x: x[index] == bit, co2_rating))
            if len(co2_rating) == 1:
                break

        oxygen_rating_ = int("".join(oxygen_rating[0]), 2)
        co2_rating_ = int("".join(co2_rating[0]), 2)
        return oxygen_rating_ * co2_rating_


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
