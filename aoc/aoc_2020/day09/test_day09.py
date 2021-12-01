import pytest
from .day09 import Day09

INPUT = \
"""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

def test_part1():
    assert Day09().load_from_string(INPUT).part1(5) == 127

def test_part2():
    assert Day09().load_from_string(INPUT).part2(5, 127) == 62