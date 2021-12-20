# aoc_day_20.py

from copy import deepcopy
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix=test_suffix)

    def _parse(self, puzzle_input):
        """Parse input"""
        enhancement, image = puzzle_input.split("\n\n")
        return enhancement, image.split("\n")

    DAY = 20

    def enhance_image(self, image, enhancement):
        new_image = deepcopy(image)

        for lineNumber, line in enumerate(image):
            if lineNumber == 0 or lineNumber == len(image) - 1:
                continue
            for position, pixel in enumerate(line):
                if position == 0 or position == len(line) - 1:
                    continue

                neighbors = self.get_neighbors(image, lineNumber, position)
                pixels = ""
                for neighbor in neighbors:
                    pixels += str(neighbor)
                index = int(pixels, 2)
                enhancement_pixel = enhancement[index]

                new_image[lineNumber][position] = enhancement_pixel

        return new_image

    @staticmethod
    def get_neighbors(image, line_number, position):
        neighbors = []

        for lineDiff in [-1, 0, 1]:
            for posDiff in [-1, 0, 1]:
                neighbors.append(image[line_number + lineDiff][position + posDiff])

        neighbors = [0 if x == "." else 1 for x in neighbors]
        return neighbors

    @staticmethod
    def prepare_image(image, addition_size):
        new_image = []
        empty_line = (
            ["." for x in range(addition_size)]
            + ["." for x in range(len(image[0]))]
            + ["." for x in range(addition_size)]
        )
        for _ in range(addition_size):
            new_image.append(deepcopy(empty_line))

        for line in image:
            new_image.append(
                ["." for x in range(addition_size)]
                + [x for x in line]
                + ["." for x in range(addition_size)]
            )

        for _ in range(addition_size):
            new_image.append(deepcopy(empty_line))

        return new_image

    def enhance_image_repeater(self, /, repeat=2):
        extended_image = self.prepare_image(self.data[1], 100)
        new_image = deepcopy(extended_image)

        for i in range(repeat):
            new_image = self.enhance_image(new_image, self.data[0])
            second_new_image = []
            for lineNumber, line in enumerate(new_image):
                if lineNumber == 0 or lineNumber == len(new_image) - 1:
                    continue
                second_new_image.append(line[1:-1])
            new_image = deepcopy(second_new_image)

        lit_pixels = 0
        for line in new_image:
            lit_pixels += len([x for x in line if x == "#"])

        return lit_pixels

    def part1(self):
        """Solve part 1"""
        return self.enhance_image_repeater()

    def part2(self):
        """Solve part 2"""
        return self.enhance_image_repeater(repeat=50)


if __name__ == "__main__":
    AocSolution().print_solution()
