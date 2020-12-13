import pytest
from .day13 import Day13

INPUT = \
"""939
7,13,x,x,59,x,31,19
"""

INPUT_P2_1 = \
"""1
17,x,13,19
"""

INPUT_P2_2 = \
"""1
67,7,59,61
"""

INPUT_P2_3 = \
"""1
67,x,7,59,61
"""

INPUT_P2_4 = \
"""1
67,7,x,59,61
"""

INPUT_P2_5 = \
"""1
1789,37,47,1889
"""

def test_part1():
    assert Day13().load_from_string(INPUT).part1() == 295

def test_part2():
    assert Day13().load_from_string(INPUT).part2() == 1068781