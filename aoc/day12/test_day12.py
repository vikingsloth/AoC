import pytest
from .day12 import Day12

INPUT = \
"""F10
N3
F7
R90
F11
"""

def test_part1():
    assert Day12().load_from_string(INPUT).part1() == 25

def test_part2():
    assert Day12().load_from_string(INPUT).part2() == 26