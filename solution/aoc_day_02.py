# aoc_day_02.py


from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return_list = list()
        for line in puzzle_input.split("\n"):
            split_line = line.split(" ")
            return_list.append((split_line[0], int(split_line[1])))

        return return_list

    def part1(self):
        """Solve part 1"""
        horizontal_position = 0
        depth = 0

        for command in self.data:
            if command[0] == "forward":
                horizontal_position += command[1]
            elif command[0] == "down":
                depth += command[1]
            elif command[0] == "up":
                depth -= command[1]

        return horizontal_position * depth

    def part2(self):
        """Solve part 2"""
        horizontal_position = 0
        depth = 0
        aim = 0

        for command in self.data:
            if command[0] == "forward":
                horizontal_position += command[1]
                depth += aim * command[1]
            elif command[0] == "down":
                aim += command[1]
            elif command[0] == "up":
                aim -= command[1]

        return horizontal_position * depth


if __name__ == "__main__":
    AocSolution("day_02.txt")
