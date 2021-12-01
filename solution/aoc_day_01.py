# aoc_day_01.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(data, group_size=1):
    """Solve part 1"""
    increasing_measurements = 0

    for index, _ in enumerate(data):
        if index <= group_size - 1:
            continue
        if sum(data[index - (group_size - 1) : index + 1]) > sum(
            data[index - group_size : index]
        ):
            increasing_measurements += 1

    return increasing_measurements


def part2(data, group_size=3):
    """Solve part 2"""
    return part1(data, group_size)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


def main():
    path = f"{pathlib.Path(__file__).parent.parent}/resources/day_01.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))


if __name__ == "__main__":
    main()
