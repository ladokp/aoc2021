# test_aoc_day_21.py

import pytest
import solution.aoc_day_21 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data == (
        aoc.Player(position=4, score=0),
        aoc.Player(position=8, score=0),
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 739785


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 444356092776315


def test_parse_exercise_solution(exercise_solution):
    """Test that input is parsed properly"""
    assert exercise_solution.data == (
        aoc.Player(position=10, score=0),
        aoc.Player(position=3, score=0),
    )


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 742257


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 93726416205179
