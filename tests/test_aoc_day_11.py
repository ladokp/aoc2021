# test_aoc_day_11.py

import pytest
import solution.aoc_day_11 as aoc

aoc_day_solution = aoc.AocSolution()
aoc_day_solution_test = aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def example1():
    return aoc_day_solution_test.data


@pytest.fixture
def exercise_data():
    return aoc_day_solution.data


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_solution_test.part1() == 1656


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 195


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1() == 1642


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 320
