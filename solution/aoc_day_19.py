# aoc_day_19.py

from collections import defaultdict
from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    P = tuple[int, int, int]
    S = tuple[str, int, int]

    def __init__(self, /, test_suffix=""):
        self.positions = {}
        self.part1_solution, self.part2_solution = None, None
        super().__init__(test_suffix=test_suffix)

    def _parse(self, puzzle_input):
        """Parse input"""
        return puzzle_input.splitlines()

    DAY = 19

    @staticmethod
    def get_pt(facing, d, rots, pt):
        da, db, dc = pt
        if facing == "x":
            main, off_a, off_b = da, db, dc
        elif facing == "y":
            main, off_a, off_b = db, dc, da
        elif facing == "z":
            main, off_a, off_b = dc, da, db

        if d == -1:
            off_a, off_b = off_b, off_a

        for _ in range(rots):
            off_a, off_b = off_b, -off_a

        return d * main, off_a, off_b

    @staticmethod
    def gen_states():
        for facing in "xyz":
            for d in (-1, 1):
                for rots in range(4):
                    yield facing, d, rots

    def solve_scanner(self, b1, b2):
        for facing, d, rots in self.gen_states():
            b2_rot = [self.get_pt(facing, d, rots, b) for b in b2]
            offsets: defaultdict[AocSolution.P, int] = defaultdict(int)
            for x1, y1, z1 in b1:
                for x2, y2, z2 in b2_rot:
                    offsets[(x1 - x2, y1 - y2, z1 - z2)] += 1

            x = list(offsets.keys())
            max_off = max(x, key=lambda x: offsets[x])

            if offsets[max_off] >= 12:
                return (facing, d, rots), max_off

        return None

    def analyze_beacons_and_scanners(self, /, enable_part2=False):
        """Solve part 1"""
        scanners: list[list[AocSolution.P]] = []
        curr_scanner: list[AocSolution.P] = []
        for line in self.data:
            if line.startswith("---"):
                curr_scanner = []
            elif line:
                x, y, z = tuple(map(int, line.split(",")))
                curr_scanner.append((x, y, z))
            else:
                scanners.append(curr_scanner)

        if curr_scanner:
            scanners.append(curr_scanner)

        self.positions[0] = (0, 0, 0)

        pts: defaultdict[AocSolution.P, int] = defaultdict(int)
        for pt in scanners[0]:
            pts[pt] += 1

        known = {0}
        unknown = set(range(len(scanners))) - {0}
        while unknown:
            found = False
            for i in known:
                for j in unknown:
                    ans = self.solve_scanner(scanners[i], scanners[j])
                    if ans is not None:
                        found = True
                        (facing, d, rots), off = ans

                        self.positions[j] = off

                        new_pts = []
                        for x, y, z in scanners[j]:
                            x, y, z = self.get_pt(facing, d, rots, (x, y, z))
                            x += off[0]
                            y += off[1]
                            z += off[2]
                            new_pts.append((x, y, z))
                            pts[x, y, z] += 1
                        scanners[j] = new_pts
                        break

                if found:
                    break

            assert found

            known.add(j)
            unknown.remove(j)

        self.part1_solution = len(pts)
        if not enable_part2:
            return

        max_dist = 0
        p = list(self.positions.values())
        for i in range(1, len(p)):
            for j in range(i):
                dist = 0
                for z in range(3):
                    dist += abs(p[i][z] - p[j][z])

                max_dist = max(max_dist, dist)

        self.part2_solution = max_dist

    def part1(self):
        """Solve part 1"""
        if not self.part1_solution or not self.part2_solution:
            self.analyze_beacons_and_scanners()
        return self.part1_solution

    def part2(self):
        """Solve part 2"""
        if not self.part1_solution or not self.part2_solution:
            self.analyze_beacons_and_scanners(enable_part2=True)
        return self.part2_solution


if __name__ == "__main__":
    AocSolution().print_solution()
