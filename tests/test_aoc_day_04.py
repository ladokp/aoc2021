# test_aoc_day_04.py

import pytest
import solution.aoc_day_04 as aoc

aoc_day_solution = aoc.AocSolution("day_04.txt")
aoc_day_solution_test = aoc.AocSolution("day_04_test.txt")


@pytest.fixture
def example1():
    return aoc_day_solution_test.drawn_numbers, aoc_day_solution_test.boards_list


@pytest.fixture
def exercise_data():
    return aoc_day_solution.drawn_numbers, aoc_day_solution.boards_list


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1[0] == [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    assert example1[1] == [
        [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc_day_solution_test.part1() == 4512


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc_day_solution_test.part2() == 1924


def test_part1_exercise_data(exercise_data):
    """Test part 1 on exercise_data input"""
    assert aoc_day_solution.part1() == 46920


def test_part2_exercise_data(exercise_data):
    """Test part 2 on exercise_data input"""
    assert aoc_day_solution.part2() == 12635
