# test_aoc_day_03.py

import pytest
import solution.aoc_day_03 as aoc

aoc_day_solution = aoc.AocSolution("day_03.txt")
aoc_day_solution_test = aoc.AocSolution("day_03_test.txt")


@pytest.fixture
def example1():
    return aoc_day_solution_test.data


@pytest.fixture
def exercise_data():
    return aoc_day_solution.data


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
    assert aoc_day_solution_test.part1()[0] == 198


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 230


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1()[0] == 2743844


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 6677951
