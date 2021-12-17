# aoc_base.py

import pathlib
from abc import ABC, abstractmethod
from pprint import pprint


class AocBaseClass(ABC):
    def __init__(self, /, test_suffix=""):
        path = f"{pathlib.Path(__file__).parent.parent}/resources/day_{self.__class__.get_day():02}{test_suffix}.txt"
        puzzle_input = pathlib.Path(path).read_text().strip()
        self.solved = False
        self.data = self._parse(puzzle_input)
        self.solutions = None

    @classmethod
    def get_day(cls):
        """Return the corresponding day to reference the correct input file"""
        return cls.DAY

    @abstractmethod
    def _parse(self, puzzle_input):
        """Parse input"""
        pass

    @abstractmethod
    def part1(self):
        """Solve part 1"""
        pass

    @abstractmethod
    def part2(self):
        """Solve part 2"""
        pass

    def print_solution(self):
        if not self.solved:
            self.solve()
        part1, part2 = self.solutions
        pprint({"part1": part1, "part2": part2})

    def solve(self):
        """Solve the puzzle for the given input"""
        self.solutions = self.part1(), self.part2()
        self.solved = True
