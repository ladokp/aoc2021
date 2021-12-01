# test_aoc_day_01.py

import pathlib
import pytest
import solution.aoc_day_01 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "resources/day_01_test.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def exercise_data():
    puzzle_input = (PUZZLE_DIR / "resources/day_01.txt").read_text().strip()
    return aoc.parse(puzzle_input)


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
    assert aoc.part1(example1) == 7


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 5


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc.part1(exercise_data) == 1139


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc.part2(exercise_data) == 1103
