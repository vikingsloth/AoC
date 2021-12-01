import pytest
from aoc.aoc_2021 import Day01

INPUT = \
"""199
200
208
210
200
207
240
269
260
263
"""

def test_part1():
    assert Day01().load_from_string(INPUT).part1() == 7

def test_part2():
    assert Day01().load_from_string(INPUT).part2() == 5
