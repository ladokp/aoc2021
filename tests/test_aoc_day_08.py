# test_aoc_day_08.py

import pytest
import solution.aoc_day_08 as aoc


@pytest.fixture
def test_solution():
    return aoc.AocSolution(test_suffix="_test")


@pytest.fixture
def exercise_solution():
    return aoc.AocSolution()


def test_parse_test_solution(test_solution):
    """Test that input is parsed properly"""
    assert test_solution.data == (
        [
            [
                "be",
                "cfbegad",
                "cbdgef",
                "fgaecd",
                "cgeb",
                "fdcge",
                "agebfd",
                "fecdb",
                "fabcd",
                "edb",
            ],
            [
                "edbfga",
                "begcd",
                "cbg",
                "gc",
                "gcadebf",
                "fbgde",
                "acbgfd",
                "abcde",
                "gfcbed",
                "gfec",
            ],
            [
                "fgaebd",
                "cg",
                "bdaec",
                "gdafb",
                "agbcfd",
                "gdcbef",
                "bgcad",
                "gfac",
                "gcb",
                "cdgabef",
            ],
            [
                "fbegcd",
                "cbd",
                "adcefb",
                "dageb",
                "afcb",
                "bc",
                "aefdc",
                "ecdab",
                "fgdeca",
                "fcdbega",
            ],
            [
                "aecbfdg",
                "fbg",
                "gf",
                "bafeg",
                "dbefa",
                "fcge",
                "gcbea",
                "fcaegb",
                "dgceab",
                "fcbdga",
            ],
            [
                "fgeab",
                "ca",
                "afcebg",
                "bdacfeg",
                "cfaedg",
                "gcfdb",
                "baec",
                "bfadeg",
                "bafgc",
                "acf",
            ],
            [
                "dbcfg",
                "fgd",
                "bdegcaf",
                "fgec",
                "aegbdf",
                "ecdfab",
                "fbedc",
                "dacgb",
                "gdcebf",
                "gf",
            ],
            [
                "bdfegc",
                "cbegaf",
                "gecbf",
                "dfcage",
                "bdacg",
                "ed",
                "bedf",
                "ced",
                "adcbefg",
                "gebcd",
            ],
            [
                "egadfb",
                "cdbfeg",
                "cegd",
                "fecab",
                "cgb",
                "gbdefca",
                "cg",
                "fgcdab",
                "egfdb",
                "bfceg",
            ],
            [
                "gcafb",
                "gcf",
                "dcaebfg",
                "ecagb",
                "gf",
                "abcdeg",
                "gaef",
                "cafbge",
                "fdbac",
                "fegbdc",
            ],
        ],
        [
            ["fdgacbe", "cefdb", "cefbgd", "gcbe"],
            ["fcgedb", "cgb", "dgebacf", "gc"],
            ["cg", "cg", "fdcagb", "cbg"],
            ["efabcd", "cedba", "gadfec", "cb"],
            ["gecf", "egdcabf", "bgf", "bfgea"],
            ["gebdcfa", "ecba", "ca", "fadegcb"],
            ["cefg", "dcbef", "fcge", "gbcadfe"],
            ["ed", "bcgafe", "cdgba", "cbgef"],
            ["gbdfcae", "bgc", "cg", "cgb"],
            ["fgae", "cfgab", "fg", "bagce"],
        ],
    )


def test_part1_test_solution(test_solution):
    """Test part 1 on example input"""
    assert test_solution.part1() == 26


def test_part2_test_solution(test_solution):
    """Test part 2 on example input"""
    assert test_solution.part2() == 61229


def test_part1_exercise_solution(exercise_solution):
    """Test part 1 on exercise_solution input"""
    assert exercise_solution.part1() == 245


def test_part2_exercise_solution(exercise_solution):
    """Test part 2 on exercise_solution input"""
    assert exercise_solution.part2() == 983026
