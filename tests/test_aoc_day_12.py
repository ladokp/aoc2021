# test_aoc_day_12.py

import pytest
from collections import defaultdict
import solution.aoc_day_12 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data is None
    assert test_solution.small_caves == {"d", "c", "b"}
    assert test_solution.great_caves == defaultdict(
        list,
        {
            "start": ["A", "b"],
            "A": ["start", "c", "b", "end"],
            "b": ["start", "A", "d", "end"],
            "c": ["A"],
            "d": ["b"],
            "end": ["A", "b"],
        },
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 10


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 36


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 4573


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 117509
