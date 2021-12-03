# test_aoc_day_03.py

import pathlib
import pytest
import solution.aoc_day_03 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent

aoc_day_solution = aoc.AocSolution("day_02.txt")
aoc_day_solution_test = aoc.AocSolution("day_02_test.txt")


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "resources/day_03_test.txt").read_text().strip()
    return aoc_day_solution_test.parse(puzzle_input)


@pytest.fixture
def exercise_data():
    puzzle_input = (PUZZLE_DIR / "resources/day_03.txt").read_text().strip()
    return aoc_day_solution.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        ["0", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "0", "1", "1", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["0", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
        ["1", "1", "1", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "0", "1", "0"],
        ["0", "1", "0", "1", "0"],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_solution_test.part1(example1)[0] == 198


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2(example1) == 230


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1(exercise_data)[0] == 2743844


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2(exercise_data) == 6677951
