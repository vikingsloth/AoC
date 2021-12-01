from aoc import Solution

class Day06(Solution):

    def part1(self):
        count = 0
        s = set()
        for ans in self.data:
            if not ans:
                count += len(s)
                s = set()
                continue
            s.update(list(ans))
        else:
            count += len(s)
        return count

    def part2(self):
        count = 0
        asets = []
        for ans in self.data:
            if not ans:
                count += len(set.intersection(*asets))
                asets = []
                continue
            asets.append(set(list(ans)))
        else:
            count += len(set.intersection(*asets))
        return count