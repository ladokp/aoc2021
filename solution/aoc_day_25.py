# aoc_day_25.py

from solution.aoc_base import AocBaseClass


class AocSolution(AocBaseClass):
    def _parse(self, puzzle_input):
        """Parse input"""
        return [list(line) for line in puzzle_input.splitlines()]

    DAY = 25

    def move_east(self):
        grid, moves = self.data, []
        dim_i, dim_j = len(grid), len(grid[0])
        for i in range(dim_i):
            for j in range(dim_j):
                if grid[i][j] == ".":
                    continue
                if grid[i][j] == "v":
                    continue
                if grid[i][(j + 1) % dim_j] != ".":
                    continue
                moves.append((i, j))
        if not moves:
            return False
        for i, j in moves:
            grid[i][j] = "."
            grid[i][(j + 1) % dim_j] = ">"
        return True

    def move_south(self):
        grid, moves = self.data, []
        dim_i, dim_j = len(grid), len(grid[0])
        for j in range(dim_j):
            for i in range(dim_i):
                if grid[i][j] == ".":
                    continue
                if grid[i][j] == ">":
                    continue
                if grid[(i + 1) % dim_i][j] != ".":
                    continue
                moves.append((i, j))
        if not moves:
            return False
        for i, j in moves:
            grid[i][j] = "."
            grid[(i + 1) % dim_i][j] = "v"
        return True

    def part1(self):
        """Solve part 1"""
        step = 1
        while True:
            res_east = self.move_east()
            res_south = self.move_south()
            if not res_east and not res_south:
                break
            step += 1
        return step

    def part2(self):
        """Solve part 2"""
        pass


if __name__ == "__main__":
    AocSolution().print_solution()
