# test_aoc_day_19.py

import pytest
import solution.aoc_day_19 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data[:27] == [
        "--- scanner 0 ---",
        "404,-588,-901",
        "528,-643,409",
        "-838,591,734",
        "390,-675,-793",
        "-537,-823,-458",
        "-485,-357,347",
        "-345,-311,381",
        "-661,-816,-575",
        "-876,649,763",
        "-618,-824,-621",
        "553,345,-567",
        "474,580,667",
        "-447,-329,318",
        "-584,868,-557",
        "544,-627,-890",
        "564,392,-477",
        "455,729,728",
        "-892,524,684",
        "-689,845,-530",
        "423,-701,434",
        "7,-33,-71",
        "630,319,-379",
        "443,580,662",
        "-789,900,-551",
        "459,-707,401",
        "",
    ]


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 79


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 3621


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 442


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 11079
