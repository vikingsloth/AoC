import pytest
from aoc.aoc_2021 import Day03

INPUT = \
"""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

def test_part1():
    assert Day03().load_from_string(INPUT).part1() == 198

#def test_part2():
#    assert Day03().load_from_string(INPUT).part2() == 230
