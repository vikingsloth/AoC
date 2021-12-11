from aoc import Solution

class SyntaxParser():
    OPEN = set("([{<")

    CLOSE = set(")}]>")

    OPEN_TO_CLOSE_MAP = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    SYNTAX_ERROR_POINT_MAP = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    SYNTAX_CLOSING_POINT_MAP = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    def __init__(self, data):
        self.data = data
        self.errors = {
            ")": 0,
            "]": 0,
            "}": 0,
            ">": 0
        }
        self.closing_scores = []
        self.stack = []
        self.valid_next_close = None
        self.parse_lines()

    def parse_lines(self):
        for line in self.data:
            invalid_c = self.find_invalid_syntax(line)
            if invalid_c:
                self.errors[invalid_c] += 1
            else:
                self.closing_scores.append(self.score_last_closing())

    def get_error_score(self):
        score = 0
        for error, count in self.errors.items():
            points = self.SYNTAX_ERROR_POINT_MAP[error]
            score += points * count                 
        return score

    def get_closing_score(self):
        self.closing_scores.sort()
        return self.closing_scores[int(len(self.closing_scores) / 2)]

    def get_last_closing(self):
        closing = []
        for c in self.stack:
            closing.insert(0, self.OPEN_TO_CLOSE_MAP[c])
        return closing

    def score_last_closing(self):
        score = 0
        for c in self.get_last_closing():
            score *= 5
            score += self.SYNTAX_CLOSING_POINT_MAP[c]
        return score

    def find_invalid_syntax(self, syntax):
        self.stack = []
        self.valid_next_close = None

        for c in syntax:
            if self.is_open(c):
                # All opens are valid
                self.stack.append(c)
                self.valid_next_close = self.OPEN_TO_CLOSE_MAP[c]
            else:
                if c != self.valid_next_close:
                    # Unexpected close, invalid
                    return c
                # Valid close, pop the open off the stack
                self.stack.pop()
                if not self.stack:
                    self.valid_next_close = None
                else:
                    self.valid_next_close = self.OPEN_TO_CLOSE_MAP[self.stack[-1]]
        return None

    def is_open(self, c):
        return c in self.OPEN


class Day10(Solution):

    def part1(self):
        return SyntaxParser(self.data).get_error_score()

    def part2(self):
        return SyntaxParser(self.data).get_closing_score()