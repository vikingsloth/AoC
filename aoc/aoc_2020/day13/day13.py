from aoc import Solution

class Day13(Solution):
    def after_load(self):
        self.start = int(self.data[0])
        buses = self.data[1].split(",")
        self.buses = []
        self.schedule = []
        for offset,bus in enumerate(buses):
            if bus == "x":
                self.schedule.append((0,offset))
                continue
            self.buses.append(int(bus))
            self.schedule.append((int(bus),offset))

    def part1(self):
        closest = None
        for bus in self.buses:
            wait = bus - (self.start % bus)
            if not closest or wait < closest[1]:
                closest = (bus, wait)
        return closest[0] * closest[1]

    # Find least common multiple in reverse order of interval times
    # to reduce iterations
    def part2(self):
        self.schedule.sort(reverse = True)
        longbus,offset = self.schedule[0]
        start = longbus - offset
        interval = 1
        for bus,offset in self.schedule:
            if not bus:
                continue
            while ((start + offset) % bus) != 0: 
                start += interval
            else:
                interval *= bus
        return start