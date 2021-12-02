from aoc import Solution

class Position():
    def __init__(self):
        self.x = 0
        self.z = 0
        self.aim = 0

    def move(self, direction, amount, aim = False):
        if direction == "forward":
            if aim:
                self.z += max(amount * self.aim, 0)
            self.x += amount
        elif direction == "down":
            if aim:
                self.aim += amount
            else:
                self.z += amount
        elif direction == "up":
            if aim:
                self.aim -= amount
                return
            if self.z == 0:
                return
            self.z -= max(amount, 0)
        

class Day02(Solution):

    def parse(self, line):
        direction, amount = line.split(" ") 
        amount = int(amount)
        return (direction, amount)

    def part1(self):
        pos = Position()
        for direction, amount in self.data:
            pos.move(direction, amount)
        return pos.x * pos.z

    def part2(self):
        pos = Position()
        for direction, amount in self.data:
            pos.move(direction, amount, aim = True)
        return pos.x * pos.z