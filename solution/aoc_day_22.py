# aoc_day_22.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        self.active = list()
        super().__init__(test_suffix=test_suffix)

    def _parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.splitlines()
        return self.i_split(puzzle_input, " x=,y.z")

    DAY = 22

    @staticmethod
    def i_split(ins, delimiters):
        to_return = []
        for line in ins:
            list_ = []
            value = ""
            for c in line:
                if c not in delimiters:
                    value += c
                else:
                    if value != "":
                        list_.append(value)
                    value = ""
            list_.append(value)
            to_return.append(list_)
        return to_return

    @staticmethod
    def point_overlap(rect, min_point, max_point):
        min_v = rect[0]
        max_v = rect[1]
        for p in [0, 1, 2]:
            if min_v[p] > max_point[p] or max_v[p] < min_point[p]:
                break
        else:
            return True
        return False

    def overlap(self, min_point, max_point):
        overlap_point = []
        for a in self.active:
            if self.point_overlap(a, min_point, max_point):
                overlap_point.append(a)

        return overlap_point

    @staticmethod
    def remove(removed, stay):
        final = []
        if stay[1][2] > removed[1][2]:

            top_max_z = stay[1][2]
            top_min_z = removed[1][2] + 1
            final.append(
                [
                    [stay[0][0], stay[0][1], top_min_z],
                    [stay[1][0], stay[1][1], top_max_z],
                ]
            )
            new_max_z = top_min_z - 1
        else:
            new_max_z = stay[1][2]

        if stay[0][2] < removed[0][2]:
            top_max_z = removed[0][2] - 1
            top_min_z = stay[0][2]
            final.append(
                [
                    [stay[0][0], stay[0][1], top_min_z],
                    [stay[1][0], stay[1][1], top_max_z],
                ]
            )
            new_min_z = top_max_z + 1
        else:
            new_min_z = stay[0][2]

        if stay[1][0] > removed[1][0]:
            right_min_x = removed[1][0] + 1
            right_max_x = stay[1][0]
            final.append(
                [
                    [right_min_x, stay[0][1], new_min_z],
                    [right_max_x, stay[1][1], new_max_z],
                ]
            )
            new_max_x = right_min_x - 1
        else:
            new_max_x = stay[1][0]

        if stay[0][0] < removed[0][0]:

            left_max_x = removed[0][0] - 1
            left_min_x = stay[0][0]
            final.append(
                [
                    [left_min_x, stay[0][1], new_min_z],
                    [left_max_x, stay[1][1], new_max_z],
                ]
            )
            new_min_x = left_max_x + 1
        else:
            new_min_x = stay[0][0]

        if stay[1][1] > removed[1][1]:
            front_max_y = stay[1][1]
            front_min_y = removed[1][1] + 1
            final.append(
                [
                    [new_min_x, front_min_y, new_min_z],
                    [new_max_x, front_max_y, new_max_z],
                ]
            )
        if stay[0][1] < removed[0][1]:
            front_max_y = removed[0][1] - 1
            front_min_y = stay[0][1]
            final.append(
                [
                    [new_min_x, front_min_y, new_min_z],
                    [new_max_x, front_max_y, new_max_z],
                ]
            )
        return final

    @staticmethod
    def area(a):
        ma = a[1]
        mi = a[0]
        return (ma[0] - mi[0] + 1) * (ma[1] - mi[1] + 1) * (ma[2] - mi[2] + 1)

    def light_cubes(self, /, total_boundary=None):
        if self.active:
            self.active = list()
        for line in self.data:
            mode = line[0]
            x = [int(line[1]), int(line[2])]
            y = [int(line[3]), int(line[4])]
            z = [int(line[5]), int(line[6])]

            min_point = [min(x), min(y), min(z)]
            max_point = [max(x), max(y), max(z)]

            if self.overlap(min_point, max_point):
                rects = self.overlap(min_point, max_point)
                for rect in rects:
                    self.active.remove(rect)
                    self.active.extend(self.remove([min_point, max_point], rect))
                if mode == "on":
                    self.active.append([min_point, max_point])
            else:
                if mode == "on":
                    self.active.append([min_point, max_point])

        if total_boundary:
            self.active = self.overlap(*total_boundary)

        total = 0
        for a in self.active:
            total += self.area(a)
        return total

    def part1(self):
        """Solve part 1"""
        return self.light_cubes(total_boundary=((-50, -50, -50), (50, 50, 50)))

    def part2(self):
        """Solve part 2"""
        return self.light_cubes()


if __name__ == "__main__":
    AocSolution().print_solution()
