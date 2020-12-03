import pytest
from aoc import Day2

INPUT = \
"""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def test_part1():
    assert Day2().load_from_string(INPUT).part1() == 2

def test_part2():
    assert Day2().load_from_string(INPUT).part2() == 1
