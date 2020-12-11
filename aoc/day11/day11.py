from aoc import Solution
import math

SEAT_OCCUPIED = '#'
SEAT_FLOOR = '.'
SEAT_EMPTY = 'L'

class Seat:
    def __init__(self, x = None, y = None, status = 'X'):
        self.x = x
        self.y = y
        self.status = status
        self.pending_status = None
        self.changed_since_last = False
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.upleft = None
        self.upright = None
        self.downleft = None
        self.downright = None

    def not_occupied(self):
        return self.status == SEAT_EMPTY or self.status == SEAT_FLOOR

    def no_adjacent_occupied(self, recurse = False):
        return self.count_occupied(limit = 1, recurse = recurse) == 0

    def or_more_occupied(self, limit = 4, recurse = False):
        return self.count_occupied(limit = limit, recurse = recurse) >= limit

    def count_occupied(self, limit = None, recurse = False):
        count = 0
        for direction in ["up","down","left","right","upleft","upright","downleft","downright"]:
            seat = getattr(self, direction)
            while seat:
                if seat.status == SEAT_OCCUPIED:
                    count += 1
                    if limit and count >= limit:
                        return count
                    break
                elif seat.status == SEAT_EMPTY:
                    break
                if not recurse:
                    break
                seat = getattr(seat, direction)
        return count

    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    # Otherwise, the seat's state does not change.
    def apply_rules(self, limit = 4, recurse = False):
        changed = False
        if self.status == SEAT_EMPTY and self.no_adjacent_occupied(recurse = recurse):
            self.change_status(SEAT_OCCUPIED)
            changed = True
        elif self.status == SEAT_OCCUPIED and self.or_more_occupied(limit = limit, recurse = recurse):
            changed = True
            self.change_status(SEAT_EMPTY)
        return changed

    def change_status(self, status):
        self.pending_status = status

    def apply_status(self):
        if self.pending_status:
            if self.status == self.pending_status:
                self.changed_since_last = False
            else:
                self.status = self.pending_status
                self.changed_since_last = True
            self.pending_status = None

    def get_coords_up(self):
        return (self.x, self.y - 1)

    def get_coords_down(self):
        return (self.x, self.y + 1)

    def get_coords_left(self):
        return (self.x - 1, self.y)

    def get_coords_right(self):
        return (self.x + 1, self.y)

    def get_coords_upleft(self):
        return (self.x - 1, self.y - 1)

    def get_coords_upright(self):
        return (self.x + 1, self.y - 1)

    def get_coords_downleft(self):
        return (self.x - 1, self.y + 1)

    def get_coords_downright(self):
        return (self.x + 1, self.y + 1)

    def __str__(self):
        return self.status

    def __repr__(self):
        return self.status


class SeatMap:
    def __init__(self, data):
        self.data = data
        self.map = []
        self.max_y = len(data)
        self.max_x = len(data[0])
        self.init_map()

    def get_seats(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                yield self.map[y][x]

    def is_valid_coords(self, x, y):
        return self.max_x > x >= 0 and self.max_y > y >= 0

    def link_seats(self):
        for seat in self.get_seats():
            for direction in ["up","down","left","right","upleft","upright","downleft","downright"]:
                nx, ny = getattr(seat, "get_coords_"+direction)()
                if self.is_valid_coords(nx, ny):
                    setattr(seat, direction, self.map[ny][nx])

    def init_map(self):
        for y in range(len(self.data)):
            self.map.append([])
            for x in range(len(self.data[y])):
                status = self.data[y][x]
                seat = Seat(x, y, status)
                self.map[y].append(seat)
        self.link_seats()

    def print_map(self):
        for row in self.map:
            print(''.join(str(s) for s in row))

    def apply_rules(self, limit = 4, recurse = False):
        changed = False
        for seat in self.get_seats():
            changed |= seat.apply_rules(limit = limit, recurse = recurse)
        for seat in self.get_seats():
            seat.apply_status()
        return changed

    def occupied_count(self):
        count = 0
        for seat in self.get_seats():
            if seat.status == SEAT_OCCUPIED:
                count += 1
        return count


class Day11(Solution):
    def parse(self, line):
        return list(line)

    def part1(self):
        sm = SeatMap(self.data)
        while True:
            changed = sm.apply_rules()
            if not changed:
                return sm.occupied_count()

    def part2(self):
        sm = SeatMap(self.data)
        count = 0
        while True:
            changed = sm.apply_rules(limit = 5, recurse = True)
            count += 1
            if not changed:
                return sm.occupied_count()