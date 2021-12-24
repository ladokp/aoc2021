# aoc_day_24.py

from functools import lru_cache
from solution.aoc_base import AocBaseClass

VS = "wxyz"


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.AX, self.DZ, self.AY = [], [], []
        self.z_budget = []
        super().__init__(test_suffix=test_suffix)

    def _parse(self, puzzle_input):
        """Parse input"""
        for lineno, line in enumerate([line_ for line_ in puzzle_input.splitlines()]):
            if "add x " in line and "add x z" not in line:
                self.AX.append(int(line.split()[2]))
            if "div z " in line:
                self.DZ.append(int(line.split()[2]))
            if "add y " in line and lineno % 18 == 15:
                self.AY.append(int(line.split()[2]))

        self.z_budget = [
            26 ** len([x for x in range(len(self.DZ)) if self.DZ[x] == 26 and x >= i])
            for i in range(len(self.DZ))
        ]

    DAY = 24
    CANDIDATES = list(range(1, 10))

    @staticmethod
    def simulate(line, state):
        state = list(state)
        cmd = line.split(" ")[0]
        if cmd == "inp":
            raise Exception("")
        a = line.split(" ")[1]
        b = line.split(" ")[2]

        def parse(x):
            if x in VS:
                return state[VS.index(x)]
            return int(x)

        if cmd == "add":
            state[VS.index(a)] += parse(b)
        if cmd == "mul":
            state[VS.index(a)] *= parse(b)
        if cmd == "div":
            state[VS.index(a)] //= parse(b)
        if cmd == "mod":
            state[VS.index(a)] %= parse(b)
        if cmd == "eql":
            state[VS.index(a)] = int(state[VS.index(a)] == parse(b))
        return tuple(state)

    @lru_cache(maxsize=None)
    def run2(self, ch, z_start, w):
        state = (w, 0, 0, z_start)
        for i in range(ch * 18 + 1, ch * 18 + 18):
            state = self.simulate(self.data[i], state)
        r = state[3]
        print(self.run(ch, z_start, w) == r)
        return r

    def run(self, ch, z, w):
        x = self.AX[ch] + (z % 26)
        z = z // self.DZ[ch]
        if x != w:
            z *= 26
            z += w + self.AY[ch]
        return z

    @lru_cache(maxsize=None)
    def search(self, ch, z_sofar):
        if ch == 14:
            if z_sofar == 0:
                return [""]
            return []
        if z_sofar > self.z_budget[ch]:
            return []
        xwi_input_be = self.AX[ch] + z_sofar % 26
        w_opts = self.CANDIDATES
        if xwi_input_be in range(1, 10):
            w_opts = [xwi_input_be]
        ret = []
        for w in w_opts:
            z_next = self.run(ch, z_sofar, w)
            nxt = self.search(ch + 1, z_next)
            for x in nxt:
                ret.append(str(w) + x)
        return ret

    def part1(self, group_size=1):
        """Solve part 1"""
        return max([int(x) for x in self.search(0, 0)])

    def part2(self, group_size=3):
        """Solve part 2"""
        return min([int(x) for x in self.search(0, 0)])


if __name__ == "__main__":
    AocSolution().print_solution()
