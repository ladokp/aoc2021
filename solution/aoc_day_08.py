# aoc_day_08.py

from itertools import permutations
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        inputs = []
        outputs = []
        for line in puzzle_input.split("\n"):
            input_str, output_str = line.split(" | ")
            inputs.append([input_ for input_ in input_str.split()])
            outputs.append([output_ for output_ in output_str.split()])
        return inputs, outputs

    # Binary encoding of segments
    SEGMENT_BINARY_MASK = [
        [1, 1, 1, 0, 1, 1, 1],  # 0
        [0, 0, 1, 0, 0, 1, 0],  # 1
        [1, 0, 1, 1, 1, 0, 1],  # 2
        [1, 0, 1, 1, 0, 1, 1],  # 3
        [0, 1, 1, 1, 0, 1, 0],  # 4
        [1, 1, 0, 1, 0, 1, 1],  # 5
        [1, 1, 0, 1, 1, 1, 1],  # 6
        [1, 0, 1, 0, 0, 1, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1],  # 9
    ]

    def decode_segment_codes(self):
        part1_total = 0
        part2_total = 0
        for inputs, outputs in zip(self.data[0], self.data[1]):
            for p in permutations("abcdefg"):
                found_solution = True
                for word in inputs:
                    code = [0] * 7
                    for letter in word:
                        code[p.index(letter)] = 1
                    if code not in AocSolution.SEGMENT_BINARY_MASK:
                        found_solution = False
                        break

                if found_solution:
                    solution = p

            output = ""
            for word in outputs:
                if len(word) not in [5, 6]:
                    part1_total += 1
                code = [0] * 7
                for letter in word:
                    code[solution.index(letter)] = 1
                output += str(AocSolution.SEGMENT_BINARY_MASK.index(code))
            part2_total += int(output)
        return part1_total, part2_total

    def part1(self):
        """Solve part 1"""
        return self.decode_segment_codes()[0]

    def part2(self):
        """Solve part 2"""
        return self.decode_segment_codes()[1]


if __name__ == "__main__":
    exercise_solution = AocSolution("day_08_test.txt")
    exercise_solution.solve()
    print("\n".join(str(solution) for solution in exercise_solution.solutions))
