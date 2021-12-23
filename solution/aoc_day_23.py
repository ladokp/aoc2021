# aoc_day_23.py

import heapq
from dataclasses import dataclass
from solution.aoc_base import AocBaseClass

A, B, C, D = range(4)
EXIT = (2, 4, 6, 8)


@dataclass(frozen=True)
class State:
    energy: int
    rooms: tuple
    hallway: tuple = (None,) * 11

    def __lt__(self, other):
        return self.energy < other.energy

    @property
    def fingerprint(self):
        return self.hallway, self.rooms

    @property
    def is_done(self):
        return all(h is None for h in self.hallway) and all(
            all(a == i for a in room) for i, room in enumerate(self.rooms)
        )


class AocSolution(AocBaseClass):
    def __init__(self, /, test_suffix=""):
        super().__init__(test_suffix=test_suffix)

    def _parse(self, puzzle_input):
        """Parse input"""
        puzzle_input = puzzle_input.splitlines()
        return tuple(
            (
                ord(puzzle_input[3][2 * i + 3]) - ord("A"),
                ord(puzzle_input[2][2 * i + 3]) - ord("A"),
            )
            for i in range(4)
        )

    DAY = 23

    @staticmethod
    def insert(tpl, i, new):
        return tpl[:i] + (new,) + tpl[i + 1 :]

    def move_amphipods(self):
        room_size = len(self.data[0])
        todo = [State(0, self.data)]
        visited = set()
        while todo:
            state = heapq.heappop(todo)
            if state.is_done:
                return state.energy
            if state.fingerprint in visited:
                continue
            visited.add(state.fingerprint)
            for ri, room in enumerate(state.rooms):
                if room and not all(a == ri for a in room):
                    a = room[-1]
                    for to, d in ((-1, -1), (11, 1)):
                        for hi in range(EXIT[ri] + d, to, d):
                            if hi in EXIT:
                                continue
                            if state.hallway[hi] is not None:
                                break
                            new = State(
                                state.energy
                                + (room_size - len(room) + 1 + abs(EXIT[ri] - hi))
                                * (10 ** a),
                                self.insert(state.rooms, ri, room[:-1]),
                                self.insert(state.hallway, hi, a),
                            )
                            if new.fingerprint not in visited:
                                heapq.heappush(todo, new)
            for i, a in enumerate(state.hallway):
                if a is None:
                    continue
                if i < EXIT[a] and any(
                    u is not None for u in state.hallway[i + 1 : EXIT[a]]
                ):
                    continue
                if i > EXIT[a] and any(
                    u is not None for u in state.hallway[EXIT[a] + 1 : i]
                ):
                    continue
                if any(u != a for u in state.rooms[a]):
                    continue
                new = State(
                    state.energy
                    + (room_size - len(state.rooms[a]) + abs(EXIT[a] - i)) * (10 ** a),
                    self.insert(state.rooms, a, (state.rooms[a] + (a,))),
                    self.insert(state.hallway, i, None),
                )
                if new.fingerprint not in visited:
                    heapq.heappush(todo, new)

    def part1(self):
        """Solve part 1"""
        return self.move_amphipods()

    def part2(self):
        """Solve part 2"""
        self.data = (
            (self.data[0][0], D, D, self.data[0][1]),
            (self.data[1][0], B, C, self.data[1][1]),
            (self.data[2][0], A, B, self.data[2][1]),
            (self.data[3][0], C, A, self.data[3][1]),
        )
        return self.move_amphipods()


if __name__ == "__main__":
    AocSolution().print_solution()
