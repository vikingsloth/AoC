import pytest
from aoc.aoc_2021 import Day02

INPUT = \
"""forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def test_part1():
    assert Day02().load_from_string(INPUT).part1() == 150

def test_part2():
    assert Day02().load_from_string(INPUT).part2() == 900
