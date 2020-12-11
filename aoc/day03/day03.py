#!/usr/bin/env python3
from aoc import Solution
import numpy

class Day03(Solution):

    def parse(self, line):
        return list(line)

    def tree_count(self, right, down):
        x = 0
        y = 0
        max_x = len(self.data[0])
        max_y = len(self.data)
        count = 0
        while y < max_y:
            x += right
            if x >= max_x:
                # Wrap to other side of map
                x = x - max_x
            y += down
            if y >= max_y:
                # Reached the end
                return count
            if self.data[y][x] == '#':
                count += 1

    def print_map(self):
        for l in self.data:
            print(''.join(l))

    def part1(self):
        return self.tree_count(3, 1)

    def part2(self):
        slopes = [
            (1, 1),
            (3, 1),
            (5, 1),
            (7, 1),
            (1, 2)
        ]
        out = []
        for slope in slopes:
            out.append(self.tree_count(slope[0], slope[1]))
        return numpy.prod(out)
