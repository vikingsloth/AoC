import pytest
from aoc import Day01

INPUT = \
"""1721
979
366
299
675
1456
"""

def test_part1():
    assert Day01().load_from_string(INPUT).part1() == 514579

def test_part2():
    assert Day01().load_from_string(INPUT).part2() == 241861950
