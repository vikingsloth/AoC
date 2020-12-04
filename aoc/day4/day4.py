#!/usr/bin/env python3
from aoc import Solution
import re

class Passport:
    REQUIRED = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    re_height = re.compile(r"(\d+)(.*)")
    re_color = re.compile(r"^#[a-f0-9]{6}$")
    re_id = re.compile(r"^\d{9}$")

    def __init__(self, text):
        self.data = {}
        self._parse_from_string(text)

    def _parse_from_string(self, text):
        pairs = text.split(" ")
        for pair in pairs:
            k,v = pair.split(":")
            self.data[k] = v

    def has_req_fields(self):
        return all(key in self.data for key in self.REQUIRED)

    def validate_field(self, field, value):
        try:
            is_valid = getattr(self, field + "_is_valid")(value)
        except AttributeError:
            # No validator exists, assume valid
            is_valid = True
        return is_valid

    def is_valid(self):
        if not self.has_req_fields():
            return False
        for field,value in self.data.items():
            if not self.validate_field(field, value):
                return False
        return True

    @staticmethod
    def _int_or_false(a):
        try:
            a = int(a)
        except ValueError:
            return False
        return a

    @staticmethod
    def byr_is_valid(a):
        a = Passport._int_or_false(a)
        return a and 1920 <= a <= 2002
    
    @staticmethod
    def iyr_is_valid(a):
        a = Passport._int_or_false(a)
        return a and 2010 <= a <= 2020
    
    @staticmethod
    def eyr_is_valid(a):
        a = Passport._int_or_false(a)
        return a and 2020 <= a <= 2030
    
    @staticmethod
    def hgt_is_valid(a):
        m = Passport.re_height.match(a)
        if not m:
            return False
        height = Passport._int_or_false(m.group(1))
        htype = m.group(2)
        if htype == "cm":
            return height and 150 <= height <= 193
        if htype == "in":
            return height and 59 <= height <= 76
        return False
    
    @staticmethod
    def hcl_is_valid(a):
        m = Passport.re_color.match(a)
        return bool(m)
    
    @staticmethod
    def ecl_is_valid(a):
        colors = ['amb','blu','brn','gry','grn','hzl','oth']
        return a in colors
    
    @staticmethod
    def pid_is_valid(a):
        m = Passport.re_id.match(a)
        return bool(m)


        

class Day4(Solution):
    def after_load(self):
        self.create_passports()

    def create_passports(self):
        self.passports = []
        current = []
        for line in self.data:
            if not line:
                self.passports.append(Passport(' '.join(current)))
                current = []
            else:
                current.append(line)
        else:
            self.passports.append(Passport(' '.join(current)))
        return self

    def part1(self):
        count = 0
        for p in self.passports:
            if p.has_req_fields():
                count += 1
        return count

    def part2(self):
        count = 0
        for p in self.passports:
            if p.is_valid():
                count += 1
        return count
