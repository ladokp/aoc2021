# aoc_day_02.py

import pathlib


def parse(puzzle_input):
    """Parse input"""
    return_list = list()
    for line in puzzle_input.split("\n"):
        split_line = line.split(" ")
        return_list.append((split_line[0], int(split_line[1])))

    return return_list


def part1(data):
    """Solve part 1"""
    horizontal_position = 0
    depth = 0

    for command in data:
        if command[0] == "forward":
            horizontal_position += command[1]
        elif command[0] == "down":
            depth += command[1]
        elif command[0] == "up":
            depth -= command[1]

    return horizontal_position * depth


def part2(data):
    """Solve part 2"""
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in data:
        if command[0] == "forward":
            horizontal_position += command[1]
            depth += aim * command[1]
        elif command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]

    return horizontal_position * depth


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)
    return solution1, solution2


def main():
    path = f"{pathlib.Path(__file__).parent.parent}/resources/day_02.txt"
    puzzle_input = pathlib.Path(path).read_text().strip()
    solutions = solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))


if __name__ == "__main__":
    main()
