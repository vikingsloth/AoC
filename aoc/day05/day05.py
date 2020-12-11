#!/usr/bin/env python3
from aoc import Solution

class Ticket:
    def __init__(self, code):
        self.code = code
        self.row_code = code[:7]
        self.seat_code = code[-3:]
        self.row = None
        self.seat = None
        self.id = None

    def bsp_parse(self, code):
        out = 0
        code = list(code)
        code.reverse()
        for i in range(len(code)):
            if code[i] == 'B' or code[i] == 'R':
                out += 1<<i
        return out

    def get_row(self):
        if self.row:
            return self.row
        self.row = self.bsp_parse(self.row_code)
        return self.row

    def get_seat(self):
        if self.seat:
            return self.seat
        self.seat = self.bsp_parse(self.seat_code)
        return self.seat

    def get_id(self):
        if self.id:
            return self.id
        self.id = self.get_row() * 8 + self.get_seat()
        return self.id


class Day05(Solution):

    def parse(self, line):
        return Ticket(line)

    def part1(self):
        highest = 0
        for ticket in self.data:
            sid = ticket.get_id()
            if sid > highest:
                highest = sid
        return highest

    def part2(self):
        sids = []
        for code in self.data:
            sid = ticket.get_id()
            sids.append(sid)
        sids.sort()
        for i in range(sids[0], sids[-1]):
            if not i in sids:
                return i
