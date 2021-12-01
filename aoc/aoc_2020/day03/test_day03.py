import pytest
from aoc.aoc_2020 import Day03

INPUT = \
"""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

def test_part1():
    assert Day03().load_from_string(INPUT).part1() == 7

def test_part2():
    assert Day03().load_from_string(INPUT).part2() == 336
