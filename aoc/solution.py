import io

class Solution:
    def __init__(self, filename = None):
        if filename:
            self.load_from_file(filename)

    # Implement this method in a subclass to customize the input parsing
    def parse(line):
        return line

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
        return self

    def load_from_string(self, s):
        f = io.StringIO(s)
        self.load_from_iter(f)
        return self


