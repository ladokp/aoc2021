# test_aoc_day_01.py

import pathlib
import pytest
import solution.aoc_day_01 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent

aoc_day_one = aoc.AocSolution("day_01.txt")
aoc_day_one_test = aoc.AocSolution("day_01_test.txt")


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "resources/day_01_test.txt").read_text().strip()
    return aoc_day_one.parse(puzzle_input)


@pytest.fixture
def exercise_data():
    puzzle_input = (PUZZLE_DIR / "resources/day_01.txt").read_text().strip()
    return aoc_day_one_test.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_one_test.part1(example1) == 7


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_one_test.part2(example1) == 5


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_one.part1(exercise_data) == 1139


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_one.part2(exercise_data) == 1103
