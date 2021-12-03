# aoc_day_02.py
import copy
import pathlib


def parse(puzzle_input):
    """Parse input"""
    return [list(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    tranposed_data = [list(i) for i in zip(*data)]
    gamma = list()
    epsilon = list()
    for bit_list in tranposed_data:
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


def part2(data):
    """Solve part 2"""
    _, gamma, epsilon = part1(data)

    oxygen_rating = copy.deepcopy(data)
    for index, _ in enumerate(gamma):
        bit = part1(oxygen_rating)[1][index]
        oxygen_rating = list(filter(lambda x: x[index] == bit, oxygen_rating))
        if len(oxygen_rating) == 1:
            break

    co2_rating = copy.deepcopy(data)
    for index, _ in enumerate(epsilon):
        bit = part1(co2_rating)[2][index]
        co2_rating = list(filter(lambda x: x[index] == bit, co2_rating))
        if len(co2_rating) == 1:
            break

    oxygen_rating_ = int("".join(oxygen_rating[0]), 2)
    co2_rating_ = int("".join(co2_rating[0]), 2)
    return oxygen_rating_ * co2_rating_


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1, _, _ = part1(data)
    solution2 = part2(data)
    return solution1, solution2


def main():
    path = f"{pathlib.Path(__file__).parent.parent}/resources/day_03_test.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))


if __name__ == "__main__":
    main()
