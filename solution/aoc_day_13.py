# aoc_day_13.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.coordinates = list()
        self.instructions = list()
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
        self.coordinates = tmp_coordinate_list

        tmp_instructions_list = list()
        for index, instruction in enumerate(self.instructions.split("\n")):
            direction, axis = instruction.split("=")
            tmp_instructions_list.append((direction[-1], int(axis)))
        self.instructions = tmp_instructions_list

    def fold_map(self, instruction):
        direction, fold_index = instruction
        new_coordinates = list()
        for coordinate in self.coordinates:
            if (direction == "y" and coordinate[1] < fold_index) or (
                direction == "x" and coordinate[0] < fold_index
            ):
                new_coordinates.append(coordinate)
            elif direction == "y":
                new_y = fold_index - (coordinate[1] - fold_index)
                new_coordinates.append((coordinate[0], new_y))
            else:
                new_x = fold_index - (coordinate[0] - fold_index)
                new_coordinates.append((new_x, coordinate[1]))
        self.coordinates = set(new_coordinates)
        return len(set(self.coordinates))

    def print_map(self):
        x_list = [c[0] for c in self.coordinates]
        max_x = max(x_list)
        y_list = [c[1] for c in self.coordinates]
        max_y = max(y_list)
        string_map = ""
        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                if (x, y) in self.coordinates:
                    string_map += "#"
                else:
                    string_map += " "
            string_map += "\n"
        return string_map

    def part1(self):
        """Solve part 1"""
        return self.fold_map(self.instructions[0])

    def part2(self):
        """Solve part 2"""
        for instruction in self.instructions:
            self.fold_map(instruction)
        return self.print_map()


if __name__ == "__main__":
    exercise_solution = AocSolution()
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
