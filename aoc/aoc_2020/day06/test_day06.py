import pytest
from .day06 import Day06

INPUT = \
"""abc

a
b
c

ab
ac

a
a
a
a

b
"""

def test_part1():
    assert Day06().load_from_string(INPUT).part1() == 11

def test_part2():
    assert Day06().load_from_string(INPUT).part2() == 6