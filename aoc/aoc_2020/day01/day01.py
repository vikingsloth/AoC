from aoc import Solution

class Day01(Solution):

    def parse(self, line):
        return int(line)

    def part1(self):
        n = self.data
        for a in range(len(n) - 1):
            for b in range(a + 1):
                if n[a] + n[b] == 2020:
                    return n[a] * n[b]

    def part2(self):
        n = self.data
        for a in range(len(n) - 1):
            for b in range(a + 1):
                for c in range(a + 1):
                    if n[a] + n[b] + n[c] == 2020:
                         return n[a] * n[b] * n[c]
