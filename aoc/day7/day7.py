from aoc import Solution
import re

class Day7(Solution):
    re_bagrule = re.compile("^(.*) bags contain (.*)$")
    re_subbag = re.compile("(\d+|no) (.*) bags?\.?")

    def after_load(self):
        self.bags = {}
        for b in self.data:
            color = b[0]
            subcolors = b[1]
            self.bags[color] = subcolors

    def parse(self, line):
        m = self.re_bagrule.match(line) 
        if not m:
            raise ValueError("Input didn't match regex for bag rule", line)
        color = m.group(1)
        contains = m.group(2).split(',')
        subcolors = {}
        for cline in contains:
            m = self.re_subbag.search(cline)
            if not m:
                raise ValueError("Input didn't match regex for sub bag rule", cline)
            count = m.group(1)
            if count == "no":
                break
            subcolor = m.group(2)
            subcolors[subcolor] = int(count)
        return (color, subcolors)

    def search_bags(self, color):
        out = set()
        subcolors = self.bags[color]
        for subcolor in subcolors:
            out.add(subcolor)
            out.update(self.search_bags(subcolor))
        return out

    def part1(self):
        count = 0
        for bag in self.bags:
            colors = self.search_bags(bag)
            if "shiny gold" in colors:
                count += 1
        return count

    def count_bags(self, color):
        nbags = 1
        colors = self.bags[color]
        for color,count in colors.items():
            nbags += count * self.count_bags(color)
        return nbags

    def part2(self):
        return self.count_bags("shiny gold") - 1