import pytest
from .day11 import Day11, Seat, SeatMap

INPUT = \
"""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

def test_part1():
    assert Day11().load_from_string(INPUT).part1() == 37

def test_part2():
    assert Day11().load_from_string(INPUT).part2() == 26