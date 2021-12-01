from aoc import Solution

class Day01(Solution):

    def parse(self, line):
        return int(line)

    def part1(self):
        if len(self.data) < 2:
            return 0
        increased = 0
        for i in range(len(self.data) - 1):
            if self.data[i] < self.data[i + 1]:
                increased += 1
        return increased

    def part2(self):
        if len(self.data) < 2:
            return 0
        increased = 0
        last_sum = sum(self.data[0:min(len(self.data), 3)])
        for i in range(1, len(self.data) - 1):
            cur_sum = sum(self.data[i:min(len(self.data), i + 3)])
            if last_sum < cur_sum:
                increased += 1
            last_sum = cur_sum
        return increased
