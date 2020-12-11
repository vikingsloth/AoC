#!/usr/bin/env python3
import re
import sys
from aoc import Solution

class Day02(Solution):
    re_passwd = re.compile(r"^(\d+)-(\d+) (\w+): (\w+)$")

    def parse(self, line):
        m = self.re_passwd.match(line)
        if not m:
            print("Error matching: ", line)
            sys.exit(-1)
        pw = {
            "low": int(m.group(1)),
            "high": int(m.group(2)),
            "letter": m.group(3),
            "password": m.group(4)
        }
        return pw

    def part1(self):
        count = 0
        for pw in self.data:
            r = pw["password"].count(pw["letter"])
            if r >= pw["low"] and r <= pw["high"]:
                count += 1
        return count

    def has_letter(self, password, letter, pos):
        if pos >= len(password):
            return False
        return password[pos] == letter

    def part2(self):
        count = 0
        for pw in self.data:
            low = self.has_letter(pw["password"], pw["letter"], pw["low"])
            high = self.has_letter(pw["password"], pw["letter"], pw["high"])
            if low ^ high:
                count += 1
        return count
