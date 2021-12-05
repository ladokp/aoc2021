# test_aoc_day_05.py

import pytest
import solution.aoc_day_05 as aoc

aoc_day_solution = aoc.AocSolution("day_05.txt")
aoc_day_solution_test = aoc.AocSolution("day_05_test.txt")


@pytest.fixture
def example1():
    return aoc_day_solution_test.data


@pytest.fixture
def exercise_data():
    return aoc_day_solution.data


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [(0, 9), (5, 9), (1, 9), (2, 9), (3, 9), (4, 9)],
        [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)],
        [(3, 4), (9, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4)],
        [(2, 1), (2, 2)],
        [(7, 0), (7, 4), (7, 1), (7, 2), (7, 3)],
        [(2, 0), (3, 1), (4, 2), (5, 3), (6, 4)],
        [(0, 9), (2, 9), (1, 9)],
        [(1, 4), (3, 4), (2, 4)],
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
        [(5, 5), (6, 4), (7, 3), (8, 2)],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_solution_test.part1() == 5


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 12


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1() == 5306


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 17787
