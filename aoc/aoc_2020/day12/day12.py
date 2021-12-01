from aoc import Solution

NORTH = 0
EAST = 90
SOUTH = 180
WEST = 270

# Multiply the distance against both x and y to get the new coords
HEADING_DEGREE_MAP = {
    NORTH: (0,-1),
    EAST: (1,0),
    SOUTH: (0,1),
    WEST: (-1,0)
}

HEADING_CODE_MAP = {
    'N': NORTH,
    'E': EAST,
    'S': SOUTH,
    'W': WEST
}

class ShipNav:
    def __init__(self):
        self.waypoint = [10, -1]
        self.heading = EAST
        self.x = 0
        self.y = 0

    def turn(self, direction, amount):
        if direction == 'L':
            amount *= -1
        self.heading += amount
        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360

    def rotate(self, direction, amount):
        my = 1
        mx = 1
        if direction == 'L':
            my = -1
        else:
            mx = -1
        for i in range(int(amount / 90)):
            self.waypoint = [self.waypoint[1] * mx, self.waypoint[0] * my]

    def forward(self, amount):
        mx = HEADING_DEGREE_MAP[self.heading][0] * amount
        my = HEADING_DEGREE_MAP[self.heading][1] * amount
        self.x += mx
        self.y += my

    def follow(self, amount):
        self.x += self.waypoint[0] * amount
        self.y += self.waypoint[1] * amount

    def move(self, action, amount):
        heading = HEADING_CODE_MAP[action]
        mx = HEADING_DEGREE_MAP[heading][0] * amount
        my = HEADING_DEGREE_MAP[heading][1] * amount
        self.x += mx
        self.y += my

    def move_waypoint(self, action, amount):
        if action == 'N':
            self.waypoint[1] -= amount
        elif action == 'E':
            self.waypoint[0] += amount
        elif action == 'S':
            self.waypoint[1] += amount
        elif action == 'W':
            self.waypoint[0] -= amount

    def action(self, text, navmode = False):
        action = text[0]
        amount = int(text[1:])
        if action == 'L' or action == 'R':
            if navmode:
                self.rotate(action, amount)
            else:
                self.turn(action, amount)
            return
        if action == 'F':
            if navmode:
                self.follow(amount)
            else:
                self.forward(amount)
            return
        if navmode:
            self.move_waypoint(action, amount)
        else:
            self.move(action, amount)


class Day12(Solution):
    def part1(self):
        shipnav = ShipNav()
        for action in self.data:
            shipnav.action(action)
        return abs(shipnav.x) + abs(shipnav.y)

    def part2(self):
        shipnav = ShipNav()
        for action in self.data:
            shipnav.action(action, navmode = True)
        return abs(shipnav.x) + abs(shipnav.y)