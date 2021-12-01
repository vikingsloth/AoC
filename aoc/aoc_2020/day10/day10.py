from aoc import Solution

# Note on part2. This problem is similar to claculating password keyspace
# or combinations of letters representing telephone numbers. The formula
# is the number of possible values to the power of the length. The number
# of values in this case is either 1 or 2 where the second value is None.
# It's essentially a powerset with some edge case invalid values
# subtracted.
# 
# Adapters adjacent to ones with a joltage difference of 3 can't be
# swapped out so for the first example set this is what sections look
# like:
#
# [(0), 1, 4], [5, 6], [7, 10], [11], [12, 15, 16, 19, (22)]
# pow(1,3) * pow(2,2) * pow(1,2) * pow(2,1) * pow(1,5) = 8
# 
# There are edge cases with sets of 3 or more because some values are
# not valid.
# [4, 7, [8, 9, 10], 11, 14]
# Numbers adjacent to the ends can't be swapped out (7, and 11)
# so [8,9,10] is the set.
# powerset is:
# [[8, 9, 10], [9, 10], [8, 10], [10], [8, 9], [9], [8], []]
# with len == 3, [] is an invalid set so subtract one from the total
# pow(2,3) - 1

class Day10(Solution):
    def parse(self, line):
        return int(line)

    def part1(self):
        one = 0
        three = 1
        self.data.sort()
        ltj = self.data[-1] + 3

        if self.data[0] == 1:
            one += 1
        else:
            three += 1

        for i in range(len(self.data) -1):
            diff = self.data[i+1] - self.data[i]
            if diff == 1:
                one += 1
            else:
                three += 1
        return one * three

    def combinations(self, seq):
        j = 0
        slen = 0
        count = 1
        for i in range(len(seq) - 1):
            diff = seq[i + 1] - seq[i]
            if diff == 1:
                slen += 1
            else:
                if not slen:
                    continue
                # Remove 1 from the length because the edge is immutable
                slen -= 1
                if slen == 3:
                    # Edge case because [] is invalid set when len == 3
                    m = pow(2, slen) - 1
                else:
                    m = pow(2, slen)
                slen = 0
                count *= m
            j = seq[i]
        return count

    def part2(self):
        self.data.sort()
        self.data.insert(0,0)
        self.data.append(self.data[-1] + 3)
        return self.combinations(self.data)