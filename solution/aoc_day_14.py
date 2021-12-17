# aoc_day_14.py

from collections import Counter
from itertools import pairwise
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.polymer = ""
        self.pair_insertion_rules = None
        super().__init__(test_suffix=test_suffix)

    DAY = 14

    def _parse(self, puzzle_input):
        """Parse input"""
        self.polymer, self.pair_insertion_rules = puzzle_input.split("\n\n")
        self.pair_insertion_rules = {
            key: value
            for key, value in (
                rule.split(" -> ") for rule in self.pair_insertion_rules.splitlines()
            )
        }

    def part1(self, steps=10):
        """Solve part 1"""
        pairs = Counter(pairwise(self.polymer))
        for _ in range(steps):
            pairs_with_mid = (
                (a, self.pair_insertion_rules[a + b], b, n)
                for (a, b), n in pairs.items()
            )
            pairs = sum(
                (
                    Counter({(a, mid): n, (mid, b): n})
                    for a, mid, b, n in pairs_with_mid
                ),
                Counter(),
            )

        double_letter_counts = Counter((self.polymer[0], self.polymer[-1]))
        for (a, b), n in pairs.items():
            double_letter_counts[a] += n
            double_letter_counts[b] += n

        letter_counts = {n // 2 for n in double_letter_counts.values()}
        return max(letter_counts) - min(letter_counts)

    def part2(self):
        """Solve part 2"""
        return self.part1(40)


if __name__ == "__main__":
    AocSolution().print_solution()
