# test_aoc_day_13.py

import pytest
import solution.aoc_day_13 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.coordinates == [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
        (4, 11),
        (6, 0),
        (6, 12),
        (4, 1),
        (0, 13),
        (10, 12),
        (3, 4),
        (3, 0),
        (8, 4),
        (1, 10),
        (2, 14),
        (8, 10),
        (9, 0),
    ]
    assert test_solution.instructions == [("y", 7), ("x", 5)]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 17


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == "#####\n#   #\n#   #\n#   #\n#####\n"


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 745


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == (
        " ##  ###  #  #   ## #### ###   ##   ## \n"
        "#  # #  # # #     # #    #  # #  # #  #\n"
        "#  # ###  ##      # ###  ###  #    #   \n"
        "#### #  # # #     # #    #  # # ## #   \n"
        "#  # #  # # #  #  # #    #  # #  # #  #\n"
        "#  # ###  #  #  ##  #    ###   ###  ## \n"
    )
