# aoc_base.py

import pathlib
from abc import ABC, abstractmethod


class AocBaseClass(ABC):
    def __init__(self, file_name):
        path = f"{pathlib.Path(__file__).parent.parent}/resources/{file_name}"
        puzzle_input = pathlib.Path(path).read_text().strip()
        self.data = self._parse(puzzle_input)
        self.solutions = self.__solve()
        print("\n".join(str(solution) for solution in self.solutions))

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

    def __solve(self):
        """Solve the puzzle for the given input"""
        return self.part1(), self.part2()
