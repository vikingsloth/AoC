from aoc import Solution

class Day03(Solution):

    def part1(self):
        ones = [0] * len(self.data[0])
        for bn in self.data:
            for i in range(len(bn)):
                if bn[i] == "1":
                    ones[i] += 1
        for i in range(len(ones)):
            if ones[i] > len(self.data) / 2:
                ones[i] = "1"
            else:
                ones[i] = "0"
        gamma = "".join(ones)
        epsilon = ""
        for c in gamma:
            if c == "1":
                epsilon += "0"
            else:
                epsilon += "1"
        return int(gamma, 2) * int(epsilon, 2)

    def part2(self):
        oxy = list(self.data)
        print(oxy)
        for i in range(len(oxy[0])):
            ones = []
            zeros = []
            print(oxy)
            for a in range(len(oxy)):
                print(a, i)
                print("oxy", oxy[a])
                if oxy[a][i] == "1":
                    ones.append(oxy[a])
                else:
                    zeros.append(oxy[a])
            if len(ones) >= len(oxy) / 2:
                oxy = ones
            else:
                oxy = zeros
            if len(oxy) == 1:
                break
        print(oxy)

        co2 = list(self.data)
        print(co2)
        for i in range(len(co2[0])):
            ones = []
            zeros = []
            print(co2)
            for a in range(len(co2)):
                print(a, i)
                print("co2", co2[a])
                if co2[a][i] == "1":
                    ones.append(co2[a])
                else:
                    zeros.append(co2[a])
            if len(ones) < len(co2) / 2:
                co2 = ones
            else:
                co2 = zeros
            if len(co2) == 1:
                break
        print(co2)
        return int(oxy[0], 2) * int(co2[0], 2)