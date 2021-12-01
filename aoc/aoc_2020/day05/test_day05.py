import pytest
from .day05 import Day05, Ticket

INPUT = \
"""FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

def test_part1():
    assert Day05().load_from_string(INPUT).part1() == 820

def test_part2():
    assert Ticket("BFFFBBFRRR").get_id() == 567
    assert Ticket("FFFBBBFRRR").get_id() == 119
    assert Ticket("BBFFBBFRLL").get_id() == 820