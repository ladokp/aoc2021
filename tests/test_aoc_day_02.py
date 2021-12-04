# test_aoc_day_02.py

import pytest
import solution.aoc_day_02 as aoc

aoc_day_solution = aoc.AocSolution("day_02.txt")
aoc_day_solution_test = aoc.AocSolution("day_02_test.txt")


@pytest.fixture
def example1():
    return aoc_day_solution_test.data


@pytest.fixture
def exercise_data():
    return aoc_day_solution.data


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
    assert aoc_day_solution_test.part1() == 150


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 900


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1() == 1383564


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 1488311643
