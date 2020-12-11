from aoc import Solution

class Instruction:
    def __init__(self, op, arg):
        self.op = op
        self.arg = int(arg)

class Computer:
    def __init__(self, instructions):
        self.i = instructions

    def exec(self):
        # Instruction Pointer
        self.eip = 0
        # Accumulator
        self.acc = 0
        # Execution History Table (Detect loops)
        et = set()
        while self.eip < len(self.i):
            if self.eip in et:
                # Loop detected
                return self.acc
            et.add(self.eip)
            instruction = self.i[self.eip]
            getattr(self, "ins_" + instruction.op)(instruction.arg)
        else:
            if self.eip == len(self.i):
                # Successful execution when instruction pointer ends +1 from end
                return True
        return False

    def ins_nop(self, a):
        self.eip += 1

    def ins_acc(self, a):
        self.acc += a
        self.eip += 1

    def ins_jmp(self, a):
        self.eip += a


class Day08(Solution):
    def parse(self, line):
        op, arg = line.split(' ')
        return Instruction(op, arg)

    def part1(self):
        return Computer(self.data).exec()

    def part2(self):
        c = Computer(self.data)
        swap = {
            "nop": "jmp",
            "jmp": "nop"
        }
        for i in self.data:
            if i.op in swap:
                i.op = swap[i.op]
                if c.exec() == True:
                    return c.acc
                i.op = swap[i.op]
        return False