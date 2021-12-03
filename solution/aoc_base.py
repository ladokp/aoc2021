# aoc_base.py

import pathlib
from abc import ABC, abstractmethod


class AocBaseClass(ABC):
    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def parse(self, puzzle_input):
        """Parse input"""
        pass

    @abstractmethod
    def part1(self, data):
        """Solve part 1"""
        pass

    @abstractmethod
    def part2(self, data):
        """Solve part 2"""
        pass

    def __solve(self, puzzle_input):
        """Solve the puzzle for the given input"""
        data = self.parse(puzzle_input)
        solution1 = self.part1(data)
        solution2 = self.part2(data)
        return solution1, solution2

    def run_aoc_solution(self):
        path = f"{pathlib.Path(__file__).parent.parent}/resources/{self.file_name}"
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = self.__solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
