# aoc_day_12.py

from collections import defaultdict, Counter
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.small_caves = set()
        self.great_caves = defaultdict(list)
        super().__init__(test_suffix=test_suffix)

    DAY = 12

    def _parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.split("\n")
        for line in puzzle_input:
            start, end = line.split("-")
            self.great_caves[start].append(end)
            self.great_caves[end].append(start)
            if start.islower() and start not in ("start", "end"):
                self.small_caves.add(start)
            if end.islower() and end not in ("start", "end"):
                self.small_caves.add(end)

    def explore(self, target, path, paths, twice):
        if path in paths:
            return 0

        if target == "end":
            paths.add(path)
            return 1

        ways = 0
        for cave in self.great_caves[target]:
            cave_counter = Counter(path)
            if (
                cave.islower()
                and cave in cave_counter
                and not (twice[0] == cave and cave_counter[cave] < twice[1])
            ):
                continue

            ways += self.explore(cave, path + (cave,), paths, twice)
        return ways

    def find_paths(self, /, max_visits=1):
        paths = set()
        for small_cave in self.small_caves:
            self.explore("start", ("start",), paths, (small_cave, max_visits))

        return len(paths)

    def part1(self):
        """Solve part 1"""
        return self.find_paths()

    def part2(self):
        """Solve part 2"""
        return self.find_paths(max_visits=2)


if __name__ == "__main__":
    AocSolution().print_solution()
