# aoc_day_13.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.coordinates = list()
        self.instructions = list()
        self.max_x = 0
        self.max_y = 0
        self.map = list()
        super().__init__(test_suffix=test_suffix)

    @classmethod
    def get_day(cls):
        return 13

    def _parse(self, puzzle_input):
        """Parse input"""
        self.coordinates, self.instructions = puzzle_input.split("\n\n")
        tmp_coordinate_list = list()
        for index, coordinate in enumerate(self.coordinates.split("\n")):
            x, y = coordinate.split(",")
            tmp_coordinate_list.append((int(x), int(y)))
        tmp_coordinate_list.sort(key=lambda x_: x_[0], reverse=True)
        self.max_x = tmp_coordinate_list[0][0]
        tmp_coordinate_list.sort(key=lambda x_: x_[1], reverse=True)
        self.max_y = tmp_coordinate_list[0][1]
        self.coordinates = tmp_coordinate_list
        tmp_instructions_list = list()
        for index, instruction in enumerate(self.instructions.split("\n")):
            direction, axis = instruction.split("=")
            tmp_instructions_list.append((direction[-1], int(axis)))
        self.instructions = tmp_instructions_list

        for y in range(0, self.max_y + 1):
            tmp_list = list()
            for x in range(0, self.max_x + 1):
                if (x, y) in self.coordinates:
                    tmp_list.append("#")
                else:
                    tmp_list.append(" ")
            self.map.append(tmp_list)

    def fold_map(self, instruction):
        new_map = list()
        dots_count = 0
        if instruction[0] == "y":
            for y in range(0, instruction[1]):
                tmp_list = list()
                for x in range(0, self.max_x + 1):
                    if self.map[self.max_y - y][x] == "#" or self.map[y][x] == "#":
                        tmp_list.append("#")
                        dots_count += 1
                    else:
                        tmp_list.append(" ")
                new_map.append(tmp_list)
            self.max_y = instruction[1] - 1
            self.map = new_map
        else:
            for y in range(0, self.max_y + 1):
                tmp_list = list()
                for x in range(0, instruction[1]):
                    if self.map[y][self.max_x - x] == "#" or self.map[y][x] == "#":
                        tmp_list.append("#")
                        dots_count += 1
                    else:
                        tmp_list.append(" ")
                new_map.append(tmp_list)
            self.max_x = instruction[1] - 1
            self.map = new_map
        return dots_count

    def print_map(self):
        string_map = ""
        for line in self.map:
            string_map = string_map + "".join(line) + "\n"
        return string_map

    def part1(self):
        """Solve part 1"""
        return self.fold_map(self.instructions.pop(0))

    def part2(self):
        """Solve part 2"""
        for instruction in self.instructions:
            self.fold_map(instruction)
        return self.print_map()


if __name__ == "__main__":
    exercise_solution = AocSolution(test_suffix="")
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
