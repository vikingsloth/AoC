import io

class Solution:
    def __init__(self, filename = None):
        if filename:
            self.load_from_file(filename)

    # implement this hook to customize line parsing
    def parse(self, line):
        return line

    # hook called after parsing is completed
    def after_load(self):
        pass

    def part1(self):
        pass

    def part2(self):
        pass

    def load_from_file(self, filename):
        self.data = []
        f = open(filename, "r")
        self.load_from_iter(f)
        return self

    def load_from_iter(self, i):
        self.data = []
        for line in i:
            line = line.strip()
            self.data.append(self.parse(line))
        self.after_load()
        return self

    def load_from_string(self, s):
        f = io.StringIO(s)
        self.load_from_iter(f)
        return self


