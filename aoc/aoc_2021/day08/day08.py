from aoc import Solution

# Singleton class that holds the heavy initialization statics to avoid burdering the main class
# every time it's initialized
class WireSegmentHelper():
    _INSTANCE = None

    # For unique length sequence strings
    LEN_TO_NUM_MAP = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }

    # For sequence lengths with multiple possible numbers
    LEN_TO_POSSIBLE = {
        5: [2, 3, 5],
        6: [0, 6, 9],
    }

    # Map nunmbers to the normal expected wire/segment configuration so it
    # can be used to calculate expected intersected set lengths
    NUM_STATIC_SET = {
        0: set("abcefg"),
        1: set("cf"),
        2: set("acdeg"),
        3: set("acdfg"),
        4: set("bcdf"),
        5: set("abdfg"),
        6: set("abdefg"),
        7: set("acf"),
        8: set("abcdefg"),
        9: set("abcdfg")
    }

    def __init__(self):
        self.intersected_count = {}
        for i in range(9):
            for a in range(i + 1, 10):
                # Populate a map of set intersection lengths between each possible combination of sets
                # for each sequence of signals.
                self.intersected_count[(i, a)] = len(self.NUM_STATIC_SET[i] & self.NUM_STATIC_SET[a])

    def __new__(self):
        if not self._INSTANCE:
            self._INSTANCE = super(WireSegmentHelper, self).__new__(self)
        return self._INSTANCE

    def get_num_from_len(self, length):
        return self.LEN_TO_NUM_MAP.get(length, None)

    def get_num_list_from_len(self, length):
        return self.LEN_TO_POSSIBLE.get(length, None)

    def get_intersect_count(self, a, b):
        return self.intersected_count.get((min(a, b), max(a, b)), None)

    def is_invalid_set(self, a, a_set, b, b_set):
        expected = self.get_intersect_count(a, b)
        if len(a_set & b_set) != expected:
            return True
        else:
            return False


class WireSegment():

    def __init__(self, unique_seqs, out_seqs):
        self.wsh = WireSegmentHelper()

        self.out_seqs = out_seqs
        self.unknown = []
        for seq in unique_seqs:
            # Sort each seq because their order is randomized between unique/out
            self.unknown.append("".join(sorted(seq)))

        self.seq_to_num_map = {}
        self.num_to_seq_map = {}
        self.seq_to_seq_set = { x : set(x) for x in self.unknown }

        self._init_unique_len_seqs()
        self._init_other_seqs()

    # Map the easy unique length strings which will be used to derive the rest
    # These are the numbers 1,4,7,8
    def _init_unique_len_seqs(self):
        tmp_unknown = []
        for seq in self.unknown:
            # Take the list of known numbers and map them to their sequence and sequence set
            num = self.wsh.get_num_from_len(len(seq))
            if num:
                # Unique length numbers
                self.seq_to_num_map[seq] = num
                self.num_to_seq_map[num] = seq
                self.seq_to_seq_set[seq] = set(seq)
            else:
                # Save the rest to process later
                tmp_unknown.append(seq)
        self.unknown = tmp_unknown

    # Map the rest of the unknown strings.
    # These are the numbers 0,2,3,5,6,9
    def _init_other_seqs(self):
        for seq in self.unknown:
            # Solve the unknown sequences by comparing their expected set intersections. If
            # any are invalid, it's not the correct one
            possible_nums = self.wsh.get_num_list_from_len(len(seq))
            seq_set = self.seq_to_seq_set[seq]
            for pos_num in possible_nums:
                if self.seq_set_is_num(seq_set, pos_num):
                    # Valid number found, save it
                    self.seq_to_num_map[seq] = pos_num
                    self.num_to_seq_map[pos_num] = seq
                    break

    # Given the set of the sequence and a number return false if any set comparison doesn't
    # match the expected number
    def seq_set_is_num(self, seq_set, num):
        for known_seq, known_num in self.seq_to_num_map.items():
            known_seq_set = self.seq_to_seq_set[known_seq]
            if self.wsh.is_invalid_set(known_num, known_seq_set, num, seq_set):
                return False
        return True

    def get_num(self):
        num_str = ""
        for out_seq in self.out_seqs:
            # Sort the segment and match it with the unique segment
            out_seq = "".join(sorted(out_seq))
            num = self.seq_to_num_map[out_seq]
            num_str += str(num)
        return int(num_str)


class Day08(Solution):

    def parse(self, line):
        unique, out = line.split(" | ")
        unique = unique.split(" ")
        out = out.split(" ")
        return (unique, out)

    def part1(self):
        count = 0
        for unique, out in self.data:
            for seq in out:
                num = WireSegmentHelper.LEN_TO_NUM_MAP.get(len(seq), None)
                if num:
                    count += 1
        return count

    def part2(self):
        num = 0
        for unique, out in self.data:
            ws = WireSegment(unique, out)
            num += ws.get_num()
        return num
