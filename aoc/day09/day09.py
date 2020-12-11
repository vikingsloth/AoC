from aoc import Solution

class SumSet:
    def __init__(self, num):
        self.s = set()
        self.num = num

    def add(self, num):
        self.s.add(num + self.num)


# Stores a queue of SumSet no longer than wlen
class SumQueue:
    def __init__(self, wlen):
        self.wlen = wlen
        self.w = []

    def add(self, num):
        if len(self.w) >= self.wlen:
            # Pop off the oldest SumSet
            self.w.pop(0)
        for ss in self.w:
            # Add the new number to the SumSet of all the previous numbers
            ss.add(num)
        self.w.append(SumSet(num))

    def has_sum(self, num):
        for ss in self.w:
            if num in ss.s:
                return True
        return False


# Sliding window sum no more than limit
class SumWindow:
    def __init__(self, wlen, limit):
        self.sum = 0
        self.wlen = wlen
        self.limit = limit
        self.w = []

    def add(self, num):
        self.w.append(num)
        self.sum += num
        while self.sum > self.limit:
            i = self.w.pop(0)
            self.sum -= i
        return self.sum

    def minmax_sum(self):
        return min(self.w) + max(self.w)


class Day09(Solution):
    def parse(self, line):
        return int(line)

    def part1(self, wlen = 25):
        sq = SumQueue(wlen)
        for i in self.data[:wlen]:
            sq.add(i)
        for i in self.data[wlen:]:
            if not sq.has_sum(i):
                return i
            sq.add(i)
        return False

    def part2(self, wlen = 25, num = 14144619):
        sw = SumWindow(wlen, num)
        for i in self.data[:wlen]:
            sw.add(i)
        for i in self.data[wlen:]:
            if sw.add(i) == num:
                return sw.minmax_sum()
        return False