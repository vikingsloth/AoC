import pytest
from aoc.aoc_2021 import Day07

INPUT = "16,1,2,0,4,2,7,1,2,14"

def test_part1():
    assert Day07().load_from_string(INPUT).part1() == 37

def test_part2():
    assert Day07().load_from_string(INPUT).part2() == 168
