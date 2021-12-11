# test_aoc_day_06.py

import pytest
import solution.aoc_day_06 as aoc

aoc_day_solution = aoc.AocSolution()


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data == {0: 0, 1: 1, 2: 1, 3: 2, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0}


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 5934


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 26984457539


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert aoc_day_solution.part1() == 351092


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert aoc_day_solution.part2() == 1595330616005
