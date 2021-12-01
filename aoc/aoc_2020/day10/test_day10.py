import pytest
from .day10 import Day10

INPUT1 = \
"""16
10
15
5
1
11
7
19
6
12
4
"""

INPUT2 = \
"""28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

def test_part1():
    assert Day10().load_from_string(INPUT2).part1() == 22 * 10

def test_part2():
    assert Day10().load_from_string(INPUT1).part2() == 8
    assert Day10().load_from_string(INPUT2).part2() == 19208