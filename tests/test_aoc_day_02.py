# test_aoc_day_01.py

import pathlib
import pytest
import solution.aoc_day_02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "resources/day_02_test.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def exercise_data():
    puzzle_input = (PUZZLE_DIR / "resources/day_02.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        ("forward", 5),
        ("down", 5),
        ("forward", 8),
        ("up", 3),
        ("down", 8),
        ("forward", 2),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 150


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 900


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc.part1(exercise_data) == 1383564


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc.part2(exercise_data) == 1488311643
