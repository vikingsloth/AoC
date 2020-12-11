import pytest
from .day08 import Day08

INPUT = \
"""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

def test_part1():
    assert Day08().load_from_string(INPUT).part1() == 5

def test_part2():
    assert Day08().load_from_string(INPUT).part2() == 8