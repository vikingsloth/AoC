import pytest
from aoc import Day3

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
    assert Day3().load_from_string(INPUT).part1() == 7

def test_part2():
    assert Day3().load_from_string(INPUT).part2() == 336
