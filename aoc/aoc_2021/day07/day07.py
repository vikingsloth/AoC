from aoc import Solution
from statistics import median
import math

class Day07(Solution):

    def parse(self, line):
        return list(map(int, line.rstrip().split(",")))

    def after_load(self):
        self.data = self.data[0]
        return

    def calculate_fuel(self, pos, cumsum = False):
        fuel = 0
        for crab in self.data:
            if cumsum:
                # I did this using cumsum but googled for math function to calculate sum of sequential ints and found gauss sum
                distance = abs(crab - pos)
                fuel += ((distance + 1) * distance) // 2
            else:
                fuel += abs(crab - pos)
        return int(fuel)

    def part1(self):
        med = median(self.data)
        return self.calculate_fuel(med)

    def part2(self):
        avg = sum(self.data) / len(self.data)
        return min(self.calculate_fuel(math.floor(avg), cumsum = True), self.calculate_fuel(math.ceil(avg), cumsum = True))
